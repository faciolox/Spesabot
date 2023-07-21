from datetime import datetime
import my_struct
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
TOKEN = "6322914505:AAGlehC0gVK7seqlU-rKPGfbU7xHR7_8fDg"
WAITING, ENTER_ITEM_TO_REMOVE = range(2)

def add_to_shoppinglist(obj: my_struct.ogg, items: dict) -> dict:
    for item in items["Items"]:
        if item["Name"] == obj.Name:
            item["Quantity"] +=1
            return items
    items["Items"].append(obj.__dict__)
    return items

def add_json(obj: my_struct.ogg):
    with open('shoppinglist.json', 'r' ) as shoplist:
        items = add_to_shoppinglist(obj, json.load(shoplist))
    with open('shoppinglist.json', 'w' ) as shoplist:
         shoplist.write(json.dumps(items, indent=4))   
def create_json():
    with open('shoppinglist.json', 'w' ) as shoplist:
        Items = {"Items": []}
        shoplist.write(json.dumps(Items, indent=4))
    
def extract_text(text):
    asd = text.split()
    out = ''
    for word in range(1, len(asd)-1):
        out += asd[word] + ' '
    return out + asd[len(asd)-1]

def add(update, context):
    item = my_struct.ogg(extract_text(update.message.text),update.message.from_user.username, datetime.now())
    add_json(item)
    update.message.reply_text(item.Name + " aggiunto alla lista della spesa")

def list(update, context ):
    with open('shoppinglist.json', 'r' ) as shoplist:
        items = json.load(shoplist)
        out= ''
        id = 1
        for item in items["Items"]:
            out = ( 'ID = ' + str(id) + '\n' + "Prodotto: " + item["Name"] + "\nAggiunto da: " + item["Addresser"] + "\nQuantitá: " + str(item["Quantity"]) + "\n\n")
            id += 1
            upd.bot.sendMessage(update.message.chat_id, out)

def remove(update, context): 
    try: 
        item_id = int(extract_text(update.message.text))
    except:
        update.message.reply_text("L'Id che hai inviato non é corretto")
    
    with open('shoppinglist.json', 'r' ) as shoplist:
        items = json.load(shoplist)
        item = items["Items"][item_id - 1]
        del items["Items"][item_id - 1]
    with open('shoppinglist.json', 'w' ) as shoplist:
         shoplist.write(json.dumps(items, indent=4))
    update.message.reply_text(item["Name"]+ ' é stato eliminato')
 
 
if __name__ == "__main__":
    create_json()
    Id=1
    upd = Updater(TOKEN)
    disp=upd.dispatcher
    disp.add_handler(CommandHandler("add", add))
    disp.add_handler(CommandHandler("list", list))
    disp.add_handler(CommandHandler("delete", remove))
    print("####\tThe bot is running\t####")

    upd.start_polling()
    upd.idle()
    
