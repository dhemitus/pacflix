user_data = [
    {
        "Id": 1,
        "Name": "Shandy",
        "Refferal": "shandy-2134"
    },
    {
        "Id": 2,
        "Name": "Cahya",
        "Refferal": "cahya-2134"
    },
    {
        "Id": 3,
        "Name": "Ana",
        "Refferal": "ana-2134"
    },
    {
        "Id": 4,
        "Name": "Bagus",
        "Refferal": "bagus-2134"
    },
]

plan_data = [
    {
        "Id": 1,
        "Name": "Basic Plan",
        "Can Stream": "True",
        "Can Download": "True",
        "Devices": 1,
        "Quality": [
            "SD"
        ],
        "Content": "3rd party movie",
        "Price": 120_000
    },
    {
        "Id": 2,
        "Name": "Standard Plan",
        "Can Stream": "True",
        "Can Download": "True",
        "Devices": 2,
        "Quality": [
            "SD",
            "HD",
        ],
        "Content": "Basic Plan + Sport Streaming",
        "Price": 160_000
    },
    {
        "Id": 3,
        "Name": "Premium Plan",
        "Can Stream": "True",
        "Can Download": "True",
        "Devices": 4,
        "Quality": [
            "SD",
            "HD",
            "UHD",
        ],
        "Content": "Standard Plan + PacFlix Original Series and Movie",
        "Price": 200_000
    },
]

user_plan = [
    {
        "Id": 1,
        "User": 1,
        "Plan": 1,
        "Months": 12,
        "Bill": 120_000
        },
    {
        "Id": 2,
        "User": 2,
        "Plan": 2,
        "Months": 24,
        "Bill":160_000
        },
    {
        "Id": 3,
        "User": 3,
        "Plan": 3,
        "Months": 5,
        "Bill": 200_000
        },
    {
        "Id": 4,
        "User": 4,
        "Plan": 1,
        "Months": 11,
        "Bill": 120_000
    }
]

class DB:
    def __init__(self, user, plan, userplan):
        self.user = user
        self.plan = plan
        self.userplan = userplan
