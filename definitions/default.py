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

        # Market
        Place(
            slug = 'market',
            name = 'Market',
            actions = [
                Action(
                    slug = 'work-for-someone',
                    name = 'Working for someone',
                    action_points = 1,
                    skills_needed = ['eloquence'],
                    checks = [
                        ActionCheckSkill(
                            skill_slug = 'eloquence',
                            difficulty = 30,
                            success = [
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'eloquence', amount = 2),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'gold', multiplier = 2),
                            ],
                            failure = [
                                ActionResultEvent(min = 0, max = 0, message = '{character} had an argument with a client and didn\'t get paid'),
                            ],
                        ),
                    ],
                ),
                Action(
                    slug = 'work-for-someone',
                    name = 'Working on the Blacksmith',
                    action_points = 1,
                    skills_needed = ['crafting'],
                    checks = [
                        ActionCheckSkill(
                            skill_slug = 'crafting',
                            difficulty = 50,
                            success = [
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'eloquence', amount = 2),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'gold', multiplier = 3),
                            ],
                            failure = [
                                ActionResultEvent(min = 0, max = 0, message = '{character} dropped melte iron on the floor and got no paid'),
                            ],
                        ),
                    ],
                ),
                Action(
                    slug = 'pickpocketing',
                    name = 'Pickpocket people on the Market',
                    action_points = 1,
                    skills_needed = ['subterfuge'],
                    checks = [
                        ActionCheckSkill(
                            skill_slug = 'subterfuge',
                            difficulty = 120,
                            success = [
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'subterfuge', amount = 2),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'gold', multiplier = 4),
                            ],
                            failure = [
                                ActionResultEvent(min = 0, max = 0, message = '{character} got caught, and recognized but managed to escape'),
                                ActionResultChangeAssetFixed(min = 0, max = 0, asset_slug = 'infamy', amount= 10),
                            ],
                        ),
                    ],
                ),
            ],
        ),

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

        # Tavern
        Place(
            slug = 'tavern',
            name = 'Tavern',
            actions = [
                Action(
                    slug = 'get-a-drink',
                    name = 'Get a drink',
                    action_points = 1,
                    skills_needed = [],
                    checks = [
                        ActionCheckAutomatic(
                            success = [
                                ActionResultAcquireCondition(min = 0, max = 0, message = '{character} is now happy drunk',
                                    condition = CharacterCondition (
                                        slug = 'happy-drunk',
                                        name = 'Happy drunk',
                                        type = 'good',
                                        description = 'Happy drunk, increased eloquence',
                                    )
                                ),
                            ],
                        ),
                    ],
                ),
                Action(
                    slug = 'juggling',
                    name = 'Juggling',
                    action_points = 1,
                    skills_needed = ['dexterity'],
                    checks = [
                        ActionCheckSkill(
                            skill_slug = 'dexterity',
                            difficulty = 10,
                            success = [
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'dexterity', amount = 1),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'gold', multiplier = 1),
                            ],
                            failure = [
                                ActionResultEvent(min = 0, max = 0, message = '{character} drop the balls over a costumer drink and got expelled from the tavern'),
                            ],
                        ),
                    ],
                ),
                Action(
                    slug = 'drunk-fighting-tournament',
                    name = 'Participate in a drunk fighting tournament',
                    action_points = 3,
                    skills_needed = [],
                    checks = [
                        ActionCheckSkill(
                            skill_slug = 'martial-arts',
                            difficulty = 125,
                            success = [
                                ActionResultEvent(min = 0, max = 10, message = '{character} has participated in a tournament, with good performance'),
                                ActionResultChangeAssetVariable(min = 0, max = 10, asset_slug = 'gold', multiplier = 2),
                                ActionResultChangeAssetVariable(min = 0, max = 10, asset_slug = 'reputation', multiplier = 2),
                                ActionResultChangeAssetVariable(min = 0, max = 10, asset_slug = 'influence', multiplier = 2),
                                ActionResultAcquireCondition(min = 11, max = 0, message = '{character} has won a tournament!!',
                                    condition = CharacterCondition (
                                        slug = 'winner',
                                        name = 'Winner',
                                        type = 'good',
                                        description = 'Winner of the drunk fighting tournament',
                                    )
                                ),
                                ActionResultChangeAssetVariable(min = 11, max = 0, asset_slug = 'gold', multiplier = 4),
                                ActionResultChangeAssetVariable(min = 11, max = 0, asset_slug = 'reputation', multiplier = 4),
                                ActionResultChangeAssetVariable(min = 11, max = 0, asset_slug = 'influence', multiplier = 4),
                            ],
                            failure = [
                                ActionResultAcquireCondition(min = 0, max = 0, message = '{character} lost tournament in the first fight!!',
                                    condition = CharacterCondition (
                                        slug = 'loser',
                                        name = 'Loser',
                                        type = 'bad',
                                        description = 'Loser of the drunk fighting tournament',
                                    )
                                ),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'gold', multiplier = -1),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'reputation', multiplier = -1),
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
                                ActionResultEvent(min = 0, max = 0, message = '{character} had an argument with the employer and got no paid'),
                            ],
                        ),
                    ],
                ),
                Action(
                    slug = 'get-wood-near-forest',
                    name = 'Get wood on a near forest',
                    action_points = 1,
                    skills_needed = ['gathering'],
                    checks = [
                        ActionCheckSkill(
                            skill_slug = 'gathering',
                            difficulty = 20,
                            success = [
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'constitution', amount = 1),
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'gathering', amount = 2),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'gold', multiplier = 1),
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
                    checks = [
                        ActionCheckSkill(
                            skill_slug = 'gathering',
                            difficulty = 20,
                            success = [
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'constitution', amount = 1),
                                ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'gathering', amount = 3),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'gold', multiplier = 3),
                            ],
                            failure = [],
                        ),
                        ActionCheckRandom(
                            probability = 20,
                            skill_slug = 'martial-arts',
                            difficulty = 50,
                            success = [
                                ActionResultEvent(min = 0, max = 0, message = '{character} was attacked by bandits, but made them flee'),
                            ],
                            failure = [
                                ActionResultEvent(min = 0, max = 0, message = '{character} was attacked by bandits, some wood stolen'),
                                ActionResultChangeAssetVariable(min = 0, max = 0, asset_slug = 'gold', multiplier = -1.5),
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
            checks = [
                ActionCheckTarget(
                    skill_slug = 'martial-arts',
                    target_skill_slug = 'martial-arts',
                    success = [
                        ActionResultTargetAcquireCondition(min = 0, max = 0,
                            message = '{character} attacks {target_character} and breaks a bone',
                            target_message = '{target_character} has been attacked and now has a broken bone',
                            condition = CharacterCondition (
                                slug = 'broken-bone',
                                name = 'Broken bone',
                                type = 'bad',
                                description = 'A broken bone, reduced physical activity',
                            )
                        ),
                    ],
                    failure = [],
                    not_found = [],
                ),
                ActionCheckSkill(
                    skill_slug = 'subterfuge',
                    difficulty = 70,
                    success = [],
                    failure = [
                        ActionResultAcquireCondition(min = 0, max = 0, message = '{character} has been caught by the guard and is now in jail',
                            condition = CharacterCondition (
                                slug = 'in-jail',
                                name = 'In Jail',
                                type = 'status',
                                description = 'In jail, cannot move',
                            )
                        ),
                        ActionResultEvent(min = 5, max = 0, message = '{character} has been recognized. There is infamy for {guild}'),
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
            checks = [
                ActionCheckTarget(
                    skill_slug = 'eloquence',
                    target_skill_slug = 'eloquence',
                    success = [
                        ActionResultChangeSkillFixed(min = 0, max = 0, skill_slug = 'eloquence', amount = 1),
                        ActionResultTargetAcquireCondition(min = 0, max = 0,
                            message = '{character} has threatened {target_character} and he/she is now afraid',
                            target_message = '{target_character} has been threatened and he/she is now afraid',
                            condition = CharacterCondition (
                                slug = 'afraid',
                                name = 'Afraid',
                                type = 'bad',
                                description = 'Afraid, reduced eloquence',
                            )
                        ),
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
                GuildAsset(slug = 'influence', name = 'Influence', value = 10000),
                GuildAsset(slug = 'reputation', name = 'Reputation', value = 10000),
                GuildAsset(slug = 'infamy', name = 'Infamy', value = 10000),
            ],
            members = [
                Character(
                    slug = 'lorenzo',
                    name = 'Lorenzo',
                    archetype = 'Guild Leader',
                    avatar_slug = 'master_1',
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
                    conditions = [],
                ),
                Character(
                    slug = 'leonardo',
                    name = 'Leonardo',
                    archetype = 'Artisan',
                    avatar_slug = 'artisan',
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
                GuildAsset(slug = 'gold', name = 'Gold', value = 1000),
                GuildAsset(slug = 'wood', name = 'Wood', value = 0),
                GuildAsset(slug = 'influence', name = 'Influence', value = 0),
                GuildAsset(slug = 'reputation', name = 'Reputation', value = 0),
                GuildAsset(slug = 'infamy', name = 'Infamy', value = 0),
            ],
            members = [
                Character(
                    slug = 'segismundo',
                    name = 'Segismundo',
                    archetype = 'Guild Leader',
                    avatar_slug = 'master_3',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 20, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 60, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 20, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 30, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 30, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 50, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 20, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 100, modifier = 0),
                    ],
                    conditions = [
                        CharacterCondition(slug = 'guild_master', name = 'Guild Master', type = 'status', description = 'The destiny of this guild is in your hands.'),
                    ],
                ),
                Character(
                    slug = 'hilda',
                    name = 'Hilda',
                    archetype = 'Priest',
                    avatar_slug = 'priest',
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
                    conditions = [
                        CharacterCondition(slug = 'bishop', name = 'Bishop', type = 'status', description = 'You command all relligious movements on the city.'),
                    ],
                ),
                Character(
                    slug = 'ludovica',
                    name = 'Ludovica',
                    archetype = 'Thief',
                    avatar_slug = 'thief',
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
                    conditions = [
                        CharacterCondition(slug = 'false_confidence', name = 'False Confidence', type = 'perm_bad', description = 'You have an unjustified confidence in yourself making you expect more than you really get.'),
                    ],
                ),
                Character(
                    slug = 'vergo',
                    name = 'Vergo',
                    archetype = 'Warrior',
                    avatar_slug = 'warrior',
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
                    conditions = [
                        CharacterCondition(slug = 'marshal', name = 'Marshal', type = 'status', description = 'You command the city guard.'),
                    ],
                ),
                Character(
                    slug = 'valerio',
                    name = 'Valerio',
                    archetype = 'Combat-Cleric',
                    avatar_slug ='combat-cleric',
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
                    conditions = [
                        CharacterCondition(slug = 'alcoholic', name = 'Alcoholic', type = 'perm_bad', description = 'Drinking alcohol usually cause you some trouble.'),
                        CharacterCondition(slug = 'pummeled', name = 'Pummeled', type = 'status', description = 'You got pummeled on a fight.'),
                        CharacterCondition(slug = 'religion_fanatic', name = 'Religion Fanatic', type = 'status', description = 'Having a bishop in your guild makes you absolutely loyal.'),
                    ],
                ),
                Character(
                    slug = 'rasida',
                    name = 'Rasida',
                    archetype = 'Erudite',
                    avatar_slug = 'erudite',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 1, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 90, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 1, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 1, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 10, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 10, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [
                        CharacterCondition(slug = 'brainiac', name = 'brainiac', type = 'perm_good', description = 'Your capacity to learn things is astonishing.'),
                    ],
                ),
                Character(
                    slug = 'egero',
                    name = 'Egero',
                    archetype = 'Wood-Cutter',
                    avatar_slug = 'wood-cutter',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 20, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 10, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 5, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 60, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 40, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 10, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [
                        CharacterCondition(slug = 'religion_fanatic', name = 'Religion Fanatic', type = 'status', description = 'Having a bishop in your guild makes you absolutely loyal.'),
                    ],
                ),
                Character(
                    slug = 'viper',
                    name = 'Viper',
                    archetype = 'Assassin',
                    avatar_slug = 'assassin',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 70, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 10, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 90, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 5, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 30, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 50, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 30, modifier = 0),
                    ],
                    conditions = [
                        CharacterCondition(slug = 'iocane_immunity', name = 'Iocane Immunity', type = 'perm_good', description = ' You spent the last few years building up an immunity to iocane powder.'),
                    ],
                 ),
                Character(
                    slug = 'vasil',
                    name = 'Vasil',
                    archetype = 'Merchant',
                    avatar_slug = 'merchant',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 10, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 80, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 5, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 40, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 5, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 20, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [
                        CharacterCondition(slug = 'master_coin', name = 'Master of Coin', type = 'status', description = 'The city trust you with his finances'),
                    ],
                 ),
                Character(
                    slug = 'enzo',
                    name = 'Enzo',
                    archetype = 'Craftsman',
                    avatar_slug = 'craftsman',
                    skills = [
                        CharacterSkill(slug = 'martial-arts', name = 'Martial Arts', value = 1, modifier = 0),
                        CharacterSkill(slug = 'eloquence', name = 'Eloquence', value = 20, modifier = 0),
                        CharacterSkill(slug = 'subterfuge', name = 'Subterfuge', value = 1, modifier = 0),
                        CharacterSkill(slug = 'gathering', name = 'Gathering', value = 15, modifier = 0),
                        CharacterSkill(slug = 'constitution', name = 'Constitution', value = 20, modifier = 0),
                        CharacterSkill(slug = 'crafting', name = 'Crafting', value = 50, modifier = 0),
                        CharacterSkill(slug = 'dexterity', name = 'Dexterity', value = 10, modifier = 0),
                        CharacterSkill(slug = 'loyalty', name = 'Loyalty', value = 90, modifier = 0),
                    ],
                    conditions = [
                        CharacterCondition(slug = 'religion_fanatic', name = 'Religion Fanatic', type = 'status', description = 'Having a bishop in your guild makes you absolutely loyal.'),
                        CharacterCondition(slug = 'master_of_crafting', name = 'Master of Crafting', type = 'perm_good', description = 'You recieve a bonification to crafting thanks to education on the matter.'),
                    ],
                ),
            ],
        ),
    ]
)
