# coding: utf-8

from games.game_defs import Game
from places.place_defs import Place
from actions.action_defs import Action


default = Game(

    # == Global game settings ==
    slug = 'Test',
    name = 'Test',

    # == Places ==
    places = [

        # Farm
        Place(
            slug = 'Farm',
            name = 'farm',
            actions = [

                Action(
                    slug = 'Farm for someone',
                    name = 'farm-for-someone',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Work on your own farm',
                    name = 'work-on-your-own-farm',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

            ],
        ),


        # Mine
        Place(
            slug = 'Mine',
            name = 'mine',
            actions = [

                Action(
                    slug = 'Work on Quarry',
                    name = 'work-on-quarry',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Get ores on a near mine',
                    name = 'get-ores-on-a-near-mine',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Get ores on a far mine',
                    name = 'get-ores-on-a-far-mine',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Get ores on an unexplored mine',
                    name = 'get-ores-on-an-unexplored-mine',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

            ],
        ),


        # Dock
        Place(
            slug = 'Dock',
            name = 'dock',
            actions = [

                Action(
                    slug = 'Fishing',
                    name = 'fishing',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Work in the dock',
                    name = 'work-in-the-dock',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Commerce',
                    name = 'commerce',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

            ],
        ),


        # Market
        Place(
            slug = 'Market',
            name = 'market',
            actions = [

                Action(
                    slug = 'Buy Luxury food for the guild',
                    name = 'buy-luxury-food-for-the-guild',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Buy a barrel of Beer for the Guild',
                    name = 'buy-a-barrel-of-beer-for-the-guild',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Working for someone',
                    name = 'working-for-someone',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Selling your own goods',
                    name = 'selling-your-own-goods',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Work on a Blacksmith',
                    name = 'work-on-a-blacksmith',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Work on a Carpentry',
                    name = 'work-on-a-carpentry',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Work on a Stone Mason',
                    name = 'work-on-a-stone-mason',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

            ],
        ),


        # Forest
        Place(
            slug = 'Forest',
            name = 'forest',
            actions = [

                Action(
                    slug = 'Work on Woodcutter',
                    name = 'work-on-woodcutter',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Get wood on a near forest',
                    name = 'get-wood-on-a-near-forest',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Get wood on a far forest',
                    name = 'get-wood-on-a-far-forest',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Get wood on an unexplored forest',
                    name = 'get-wood-on-an-unexplored-forest',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Hunting on Safe Zone',
                    name = 'hunting-on-safe-zone',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Hunting on Dangerous Zone',
                    name = 'hunting-on-dangerous-zone',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

            ],
        ),


        # Church
        Place(
            slug = 'Church',
            name = 'church',
            actions = [

                Action(
                    slug = 'Pray',
                    name = 'pray',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Donate Money',
                    name = 'donate-money',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

            ],
        ),


        # Tavern
        Place(
            slug = 'Tavern',
            name = 'tavern',
            actions = [

                Action(
                    slug = 'Waiter/Waitress',
                    name = 'waiter-waitress',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Get a drink',
                    name = 'get-a-drink',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Get a meal',
                    name = 'get-a-meal',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Pay for a bath',
                    name = 'pay-for-a-bath',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Participate on Drunk Fighting Tournament',
                    name = 'participate-on-drunk-fighting-tournament',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Bet money',
                    name = 'bet-money',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Pay a round for everyone',
                    name = 'pay-a-round-for-everyone',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

                Action(
                    slug = 'Pay a fest for everyone',
                    name = 'pay-a-fest-for-everyone',
                    action_points = 1,
                    skills_needed = [],
                    skills_upgraded = ['loyalty'],
                ),

            ],
        ),


    ],

    # == Free actions ==
    free_actions = [

        Action(
            slug = 'Break Bone',
            name = 'break-bone',
            action_points = 1,
            skills_needed = ['martial-arts', 'stealth'],
            skills_upgraded = ['martial-arts', 'stealth'],
        ),

        Action(
            slug = 'Poison someone',
            name = 'poison-someone',
            action_points = 1,
            skills_needed = ['martial-arts', 'stealth'],
            skills_upgraded = ['martial-arts', 'stealth'],
        ),

        Action(
            slug = 'Blackmail',
            name = 'blackmail',
            action_points = 1,
            skills_needed = ['martial-arts', 'stealth'],
            skills_upgraded = ['martial-arts', 'stealth'],
        ),

        Action(
            slug = 'Threaten',
            name = 'threaten',
            action_points = 1,
            skills_needed = ['martial-arts', 'stealth'],
            skills_upgraded = ['martial-arts', 'stealth'],
        ),

        Action(
            slug = 'Kidnap',
            name = 'kidnap',
            action_points = 1,
            skills_needed = ['martial-arts', 'stealth'],
            skills_upgraded = ['martial-arts', 'stealth'],
        ),

        Action(
            slug = 'Ask for protection',
            name = 'ask-for-protection',
            action_points = 1,
            skills_needed = ['martial-arts', 'stealth'],
            skills_upgraded = ['martial-arts', 'stealth'],
        ),

        Action(
            slug = 'Spread Rumor',
            name = 'spread-rumor',
            action_points = 1,
            skills_needed = ['martial-arts', 'stealth'],
            skills_upgraded = ['martial-arts', 'stealth'],
        ),

    ]
)
