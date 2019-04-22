# Extract data from JSON using Xpath approach

## Background
In python to extract a value from JSON structure we have to write obj['key'] or obj[index] and it gets even more convoluted when we try to extract
a value based on certain conditions 

## Goal
This library tries to simplify extracting data from JSON using xpath like approach which are pretty much 1 liners


## How does it work
```
xpath_json.extract('spouse/firstName', input) #Extract Spouse firstName
xpath_json.extract('addresses/#', input) #Extract number of addresses
xpath_json.extract('addresses/#[description==home]', input) #Extract home address
xpath_json.extract('addresses/#[postalCode==30305]/#', input) #Extract addresses based on postalCode
xpath_json.extract('phoneNumbers/#[description==mobile]/0/number', input) #Extract first mobile number
xpath_json.extract('fav.movie', input) #Extract fav.movie (key has a .)
xpath_json.extract('friends/#[age >= 47]/#', input) #Extract based on a condition and count number of friends found
xpath_json.extract('friends/#[age<47]/#', input) #Extract based on a condition (notice no spaces)
xpath_json.extract('friends/#/firstName', input) # Extract a list of friends first names
```
### Sample Data
```
input = 
{
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
}
```