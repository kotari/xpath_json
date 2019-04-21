# Describe xpath_json project and how to use it to extract values from json
## Goal
Simplify extracting data from JSON using xpath like approach
Here I chose the delimiter to be **'/'** and not **'.'** as document can have a '.' in the key attribute 
### Sample Data
```{
    "firstName": "John",
    "lastName": "Smith",
    "age": 42,
    "spouse": {
        "firstName": "Mary",
        "lastName": "Smith",
        "age": 40
    },
    "fav.movie": "Mr & Mrs Smith",
    "addresses": [
        {
            "description": "home",
            "street": "123 Peachtree Ln",
            "city": "Atlanta",
            "state": "GA",
            "postalCode": 30305
        },
        {
            "description": "work",
            "street": "456 Peachtree St",
            "city": "Atlanta",
            "state": "GA",
            "postalCode": 30305
        }
    ],
    "phoneNumbers": [
        {
            "description": "home",
            "number": "404-555-1234"
        },
        {
            "description": "mobile",
            "number": "678-555-1234"
        }
    ],
    "friends": [
        {"firstName": "Dale", "lastName": "Murphy", "age": 44},
        {"firstName": "Roger", "lastName": "Craig", "age": 68},
        {"firstName": "Jane", "lastName": "Murphy", "age": 47}
    ]
}```