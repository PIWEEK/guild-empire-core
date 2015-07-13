from games.game_defs import Game
from places.place_defs import Place
from actions.action_defs import Action


default = Game(

    # == Global game settings ==
    slug = 'default',
    name = 'Default game definition',

    # == Places ==
    places = [

        # Church
        Place(
            slug = 'church',
            name = 'Church',
            actions = [
                Action(
                    slug = 'pray',
                    name = 'Pray',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),
                Action(
                    slug = 'donate-money',
                    name = 'Donate money',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),
            ],
        ),

        # Forest
        Place(
            slug = 'forest',
            name = 'Forest',
            actions = [
                Action(
                    slug = 'work-on-woodcutter',
                    name = 'Work on woodcutter',
                    action_points = 2,
                    skills_needed = ['constitution', 'gathering'],
                    skills_upgraded = ['constitution', 'gathering'],
                ),
                Action(
                    slug = 'get-wood-near-forest',
                    name = 'Get wood on a near forest',
                    action_points = 1,
                    skills_needed = ['constitution', 'gathering'],
                    skills_upgraded = ['constitution', 'gathering'],
                ),
                Action(
                    slug = 'get-wood-far-forest',
                    name = 'Get wood on a far forest',
                    action_points = 2,
                    skills_needed = ['constitution', 'gathering', 'martial-arts'],
                    skills_upgraded = ['constitution', 'gathering'],
                ),
            ],
        ),

    ],

    # == Free actions ==
    free_actions = [
        Action(
            slug = 'break-bone',
            name = 'Break bone',
            action_points = 1,
            skills_needed = ['martial-arts', 'stealth'],
            skills_upgraded = ['martial-arts', 'stealth'],
        ),
        Action(
            slug = 'threaten',
            name = 'Threaten',
            action_points = 1,
            skills_needed = ['eloquence', 'martial-arts'],
            skills_upgraded = ['eloquence'],
        ),
    ]
)

