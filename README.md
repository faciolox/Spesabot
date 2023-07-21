# SPESABOT

This repository contains a telegram bot written in python language which I use to have a shopping list shared with my friend/family.

The bot is meant to be used by italian speakers, so the reply message will be in Italian

The shopping list will be saved into the shoppinglist.json file

## How to use

The bot is meant to be private. So you have to insert the bot Token inside the variable TOKEN which is in the main.py file.

To be active you can just run the file main.py by opening a terminal, going into the directory which contains the repository and then write the command $ python3 main.py

## Commands

There are now three commands

### /add (item)

Writing the command /add (item) the bot will save the item into the json file

### /list

The command /list will show all the item in the shopping list in order of addition to the list. 

For each product the bot will show the Id (index in the list + 1), the name of the product, the telegram user who added the item and the quantity.

### /delete (id)

The command /delete (id) will delete an item, given an id by the user. The id represent the index of the item into the shopping list, and it can be shown by writing /list