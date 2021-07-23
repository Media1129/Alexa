import json
import csv
import random

# file path
first_turn_file = "./data/recipe_first_turn.csv"

train_slot_file = "train_aug.json"
dev_slot_file = "dev.json"
test_slot_file = "test.json"

train_save_file = "train.txt"
dev_save_file = "dev.txt"
test_save_file = "test.txt"



# open *.json file
with open(train_slot_file) as f:
    train_slot = json.load(f)

with open(dev_slot_file) as f:
    dev_slot = json.load(f)

with open(test_slot_file) as f:
    test_slot = json.load(f)


# output list
train_txt = []
dev_txt = []
test_txt = []


for idx, item in enumerate(train_slot):
    for token_idx, token in enumerate(item['tokens']):
        line_str = token+" "+item['tags'][token_idx]
        train_txt.append(line_str)
    train_txt.append("")
    
for idx, item in enumerate(dev_slot):
    for token_idx, token in enumerate(item['tokens']):
        line_str = token + " " + item['tags'][token_idx]
        dev_txt.append(line_str)
    dev_txt.append("")

for idx, item in enumerate(test_slot):
    for token_idx, token in enumerate(item['tokens']):
        line_str = token + " " + item['tags'][token_idx]
        test_txt.append(line_str)
    test_txt.append("")

    


with open(train_save_file, 'w') as f:
    for idx, sent in enumerate(train_txt):
        f.write(sent+'\n')
        

with open(dev_save_file, 'w') as f:
    for idx, sent in enumerate(dev_txt):
        f.write(sent+'\n')
        

with open(test_save_file, 'w') as f:
    for idx, sent in enumerate(test_txt):
        f.write(sent+'\n')
