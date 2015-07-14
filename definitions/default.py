from games.game_defs import Game
from places.place_defs import Place
from actions.action_defs import Action
from guilds.guild_defs import Guild, GuildAsset
from characters.character_defs import Character, CharacterSkill, CharacterCondition


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
    ],

    # == Initial guilds ===
    guilds = [
        Guild(
            slug = 'medici',
            name = 'Médici',
            assets = [
                GuildAsset(slug = 'gold', name = 'Gold', value = 10000),
                GuildAsset(slug = 'reputation', name = 'Reputation', value = 10000),
                GuildAsset(slug = 'infamy', name = 'Infamy', value = 10000),
            ],
            members = [
                Character(
                    slug = 'lorenzo',
                    name = 'Lorenzo',
                    archetype = 'Guild Leader',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 20, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 90, modifier = 0),
                        CharacterSkill(slug = 'stealth', name = 'Stealth', value = 30, modifier = 0),
                    ],
                    conditions = [
                        CharacterCondition(slug = 'governor', name = 'Governor', type = 'status', description = 'Governor of the City'),
                    ],
                ),
                Character(
                    slug = 'leonardo',
                    name = 'Leonardo',
                    archetype = 'Artisan',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 10, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 60, modifier = 0),
                        CharacterSkill(slug = 'stealth', name = 'Stealth', value = 50, modifier = 0),
                    ],
                    conditions = [],
                ),
            ],
        ),
        Guild(
            slug = 'malatesta',
            name = 'Malatesta',
            assets = [
                GuildAsset(slug = 'gold', name = 'Gold', value = 10000),
                GuildAsset(slug = 'reputation', name = 'Reputation', value = 10000),
                GuildAsset(slug = 'infamy', name = 'Infamy', value = 10000),
            ],
            members = [
                Character(
                    slug = 'segismundo',
                    name = 'Segismundo',
                    archetype = 'Guild Leader',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 80, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 20, modifier = 0),
                        CharacterSkill(slug = 'stealth', name = 'Stealth', value = 50, modifier = 0),
                    ],
                    conditions = [],
                ),
                Character(
                    slug = 'francesco',
                    name = 'Francesco',
                    archetype = 'Cleric',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 5, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 70, modifier = 0),
                        CharacterSkill(slug = 'stealth', name = 'Stealth', value = 40, modifier = 0),
                    ],
                    conditions = [],
                ),
            ],
        ),
    ]
)
