from games.game_defs import Game
from places.place_defs import Place
from actions.action_defs import *
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
                    checks = [
                        ActionCheckAutomatic(
                            success = [
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'loyalty', amount = 1),
                                ActionResultChangeAssetFixed(min = 0, max = 0, asset_slug = 'reputation', amount = 5),
                            ],
                        ),
                    ],
                ),
                Action(
                    slug = 'donate-money',
                    name = 'Donate money',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = [],
                    checks = [
                        ActionCheckAutomatic(
                            success = [
                                ActionResultChangeAssetFixed(min = 0, max = 0, asset_slug = 'gold', amount = -100),
                                ActionResultChangeAssetFixed(min = 0, max = 0, asset_slug = 'reputation', amount = 10),
                                ActionResultChangeAssetFixed(min = 0, max = 0, asset_slug = 'influence', amount = 5),
                            ],
                        ),
                    ],
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
                    skills_needed = ['gathering'],
                    skills_upgraded = ['constitution', 'gathering'],
                    checks = [
                        ActionCheckSkill(
                            skill_slug = 'gathering',
                            difficulty = 20,
                            success = [
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'constitution', amount = 1),
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'gathering', amount = 2),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'gold', multiplier = 2),
                            ],
                            failure = [
                                ActionResultEvent(min = 0, max = 0, text = '{character} had an argument with the employer and got no paid'),
                            ],
                        ),
                    ],
                ),
                Action(
                    slug = 'get-wood-near-forest',
                    name = 'Get wood on a near forest',
                    action_points = 1,
                    skills_needed = ['gathering'],
                    skills_upgraded = ['constitution', 'gathering'],
                    checks = [
                        ActionCheckSkill(
                            skill_slug = 'gathering',
                            difficulty = 20,
                            success = [
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'constitution', amount = 1),
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'gathering', amount = 2),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'wood', multiplier = 1),
                            ],
                            failure = [],
                        ),
                    ],
                ),
                Action(
                    slug = 'get-wood-far-forest',
                    name = 'Get wood on a far forest',
                    action_points = 2,
                    skills_needed = ['gathering', 'martial-arts'],
                    skills_upgraded = ['constitution', 'gathering'],
                    checks = [
                        ActionCheckSkill(
                            skill_slug = 'gathering',
                            difficulty = 20,
                            success = [
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'constitution', amount = 1),
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'gathering', amount = 3),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'wood', multiplier = 3),
                            ],
                            failure = [],
                        ),
                        ActionCheckRandom(
                            probability = 20,
                            skill_slug = 'martial-arts',
                            difficulty = 50,
                            success = [
                                ActionResultEvent(min = 0, max = 0, text = '{character} was attacked by bandits, but made them flee'),
                            ],
                            failure = [
                                ActionResultEvent(min = 0, max = 0, text = '{character} was attacked by bandits, some wood stolen'),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'wood', multiplier = -1.5),
                            ],
                            not_happen = [],
                        ),
                    ],
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
            skills_needed = ['martial-arts', 'subterfuge'],
            skills_upgraded = ['martial-arts', 'subterfuge'],
            checks = [
                ActionCheckTarget(
                    skill_slug = 'martial-arts',
                    target_skill_slug = 'martial-arts',
                    success = [
                        ActionResultEvent(min = 0, max = 0, text = '{target} now has a broken bone'),
                        ActionResultTargetAcquireCondition(min = 0, max = 0, condition = CharacterCondition (
                            slug = 'broken-bone',
                            name = 'Broken bone',
                            type = 'bad',
                            description = 'A broken bone, reduced physical activity',
                        )),
                    ],
                    failure = [],
                    not_found = [],
                ),
                ActionCheckSkill(
                    skill_slug = 'subterfuge',
                    difficulty = 70,
                    success = [],
                    failure = [
                        ActionResultEvent(min = 0, max = 0, text = '{character} has been caught by the guard and is now in jail'),
                        ActionResultTargetAcquireCondition(min = 0, max = 0, condition = CharacterCondition (
                            slug = 'in-jail',
                            name = 'In Jail',
                            type = 'status',
                            description = 'In jail, cannot move',
                        )),
                        ActionResultEvent(min = 5, max = 0, text = '{character} has been recognized. There is infamy for {guild}'),
                        ActionResultChangeAssetFixed(min = 5, max = 0, asset_slug = 'reputation', amount = -100),
                        ActionResultChangeAssetFixed(min = 5, max = 0, asset_slug = 'infamy', amount = 100),
                    ],
                ),
            ],
        ),
        Action(
            slug = 'threaten',
            name = 'Threaten',
            action_points = 1,
            skills_needed = ['eloquence'],
            skills_upgraded = ['eloquence'],
            checks = [
                ActionCheckTarget(
                    skill_slug = 'eloquence',
                    target_skill_slug = 'eloquence',
                    success = [
                        ActionResultEvent(min = 0, max = 0, text = '{target} now is afraid'),
                        ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'eloquence', amount = 1),
                        ActionResultTargetAcquireCondition(min = 0, max = 0, condition = CharacterCondition (
                            slug = 'afraid',
                            name = 'Afraid',
                            type = 'bad',
                            description = 'Afraid, reduced eloquence',
                        )),
                    ],
                    failure = [],
                    not_found = [],
                ),
            ],
        ),
    ],

    # == Initial guilds ===
    guilds = [
        Guild(
            slug = 'medici',
            name = 'Médici',
            color = 'red',
            assets = [
                GuildAsset(slug = 'gold', name = 'Gold', value = 10000),
                GuildAsset(slug = 'wood', name = 'Wood', value = 10000),
                GuildAsset(slug = 'influence', name = 'Influence', value = 10000),
                GuildAsset(slug = 'reputation', name = 'Reputation', value = 10000),
                GuildAsset(slug = 'infamy', name = 'Infamy', value = 10000),
            ],
            members = [
                Character(
                    slug = 'lorenzo',
                    name = 'Lorenzo',
                    archetype = 'Guild Leader',
                    archetype_slug = 'guild-leader',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 20, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 90, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 30, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 10, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 30, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [
                        CharacterCondition(slug = 'governor', name = 'Governor', type = 'status', description = 'Governor of the City'),
                    ],
                ),
                Character(
                    slug = 'leonardo',
                    name = 'Leonardo',
                    archetype = 'Artisan',
                    archetype_slug = 'artisan',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 10, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 60, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 5, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 6, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 80, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 30, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 20, modifier = 0),
                   ],
                   conditions = [],
                ),
            ],
        ),
        Guild(
            slug = 'malatesta',
            name = 'Malatesta',
            color = 'blue',
            assets = [
                GuildAsset(slug = 'gold', name = 'Gold', value = 10000),
                GuildAsset(slug = 'wood', name = 'Wood', value = 10000),
                GuildAsset(slug = 'influence', name = 'Influence', value = 10000),
                GuildAsset(slug = 'reputation', name = 'Reputation', value = 10000),
                GuildAsset(slug = 'infamy', name = 'Infamy', value = 10000),
            ],
            members = [
                Character(
                    slug = 'segismundo',
                    name = 'Segismundo',
                    archetype = 'Guild Leader',
                    archetype_slug = 'guild-leader',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 80, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 20, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 50, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 20, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 30, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [],
                ),
                Character(
                    slug = 'francesco',
                    name = 'Francesco',
                    archetype = 'Cleric',
                    archetype_slug = 'cleric',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 5, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 70, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 40, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 30, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 30, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [],
                ),
                Character(
                    slug = 'roger',
                    name = 'Roger',
                    archetype = 'Thief',
                    archetype_slug = 'thief',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 40, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 50, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 80, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 5, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 30, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [],
                ),
                Character(
                    slug = 'vergo',
                    name = 'Vergo',
                    archetype = 'Warrior',
                    archetype_slug = 'warrior',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 80, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 50, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 55, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 5, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 30, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [],
                ),
                Character(
                    slug = 'valerio',
                    name = 'Valerio',
                    archetype = 'Combat-Cleric',
                    archetype_slug ='combat-cleric',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 80, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 50, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 55, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 5, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 30, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [],
                ),
                Character(
                    slug = 'rasida',
                    name = 'Rasida',
                    archetype = 'Erudite',
                    archetype_slug = 'erudite',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 10, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 100, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 5, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 5, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 30, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [],
                ),
                Character(
                    slug = 'egero',
                    name = 'Egero',
                    archetype = 'Wood-Cutter',
                    archetype_slug = 'wood-cutter',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 30, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 20, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 5, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 60, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 30, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [],
                ),
                Character(
                    slug = 'viper',
                    name = 'Viper',
                    archetype = 'Assassin',
                    archetype_slug = 'assassin',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 70, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 40, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 80, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 5, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 30, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [],
                 ),
                Character(
                    slug = 'vasil',
                    name = 'Vasil',
                    archetype = 'Merchant',
                    archetype_slug = 'merchant',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 10, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 80, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 5, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 40, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 30, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [],
                 ),
                Character(
                    slug = 'ezchio',
                    name = 'Ezchio',
                    archetype = 'Craftsman',
                    archetype_slug = 'craftsman',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 10, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 30, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 5, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 50, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 30, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [],
                ),
            ],
        ),
    ]
)
