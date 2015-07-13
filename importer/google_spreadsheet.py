# coding: utf-8
"""
A XLS parser based on an iteration of the actions spreadhseet:
https://docs.google.com/spreadsheets/d/1_Kzzc4QZUr9nDtdY7P6nsjJWkeqim2Q8-jWWRvfK90A/edit#gid=0

We could consider a sheet/row notation to allow easy changes in the
game object. This way the content team can work on a spreadhseet instead
of a large file faster, and we only need parsing the thing.
"""


# python
import uuid
import copy

# third party
from jinja2 import Environment, PackageLoader
from openpyxl import load_workbook
import requests
from slugify import slugify


# == main ==
env = Environment()
template_string = open('template.j2', 'rb').read()
template = env.from_string(template_string)

# == configuration ==
DOCUMENT_ID = '1_Kzzc4QZUr9nDtdY7P6nsjJWkeqim2Q8-jWWRvfK90A'
SHEETS = ['Events', 'Conditions']


# == helper methods ==
def get_xlsx():
    url = 'https://docs.google.com/spreadsheets/d/{}/export?format=xlsx'.format(
        DOCUMENT_ID)
    path = '/tmp/{}'.format(uuid.uuid4())

    r = requests.get(url)
    handler = open(path, 'wb')

    print(url)

    with handler as fd:
        for chunk in r.iter_content(255):
            fd.write(chunk)

    return open(path, 'rb')


wb = load_workbook(get_xlsx())
context = {
    'game': {
        'name': 'Test'
    },
    'places': {}
}

# == Parse events ==
ws = wb['Events']
first_row = True
for row in ws.rows:
    if first_row:
        first_row = False
        continue
    else:
        if row[2].value:
            # Get values
            if row[0].value:
                tier = row[0].value

            if row[1].value:
                place = row[1].value
                place_slug = slugify(place)

            name = row[2].value
            slug = slugify(name)

            if row[3].value:
                skills_needed = row[3].value.lower().replace(', ', ',').strip()

            if row[4].value:
                skills_upgraded = row[4].value.lower().replace(', ', ',').strip()

            # Parse needed values
            if skills_needed and isinstance(row[3].value, unicode):
                skills_needed = skills_needed.split(',')

            if skills_upgraded and isinstance(row[4].value, unicode):
                skills_upgraded = skills_upgraded.split(',')

            # Store place if not in object yet
            if place_slug not in context['places']:
                context['places'][place_slug] = {
                    'slug': place_slug,
                    'name': place,
                    'actions': [],
                }

            # Store place events
            context['places'][place_slug]['actions'].append({
                'name': name,
                'slug': slug,
                'skills_upgraded': skills_upgraded,
                'skills_needed': skills_needed,
            })
context['free_actions'] = copy.copy(context['places']['free']['actions'])
del context['places']['free']

handler = open('game.py', 'wb')
handler.write(template.render(context))
handler.close()
