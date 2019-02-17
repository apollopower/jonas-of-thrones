# Jonas of Thrones

Since the Game of Thrones API didn't include image URLs for characters,
I made my own API! :D

Currently being hosted as a Heroku app

[Check it out here!](https://jonas-of-thrones.herokuapp.com)

## How to Use

The API takes a specific character name and returns an URL with an image
from the Westeros Wiki page.

You can make your search query by hitting:

```
https://jonas-of-thrones.herokuapp.com/image?name=<full_character_name_here>
```

Be sure to include the character's full name, separated by a space. Examples would be:

```
Jon Snow
Robb Stark
Tyrion Lannister
```