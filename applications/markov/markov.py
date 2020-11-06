import random

# Read in all the words in one go
with open("applications/markov/input.txt") as f:
    words = f.read()

word_list = words.rsplit()
word_set = list(set(word_list))


table = {}

            
def append_value(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value


for x in word_set:
    table[x] = []

for x in range(len(word_list)-1):
    append_value(table,word_list[x],word_list[x+1])

def print_sent(starter):
    b = starter
    a = ""
    count = 0
    while count < 10:
        b = random.choice(table[b])
        a += f" {b}"
        count += 1
    return a

# a = random.choice(table['like'])
# b = random.choice(table[a])
# c = random.choice(table[b])

print(print_sent(random.choice(table[random.choice(word_set)])))
print(print_sent(random.choice(table[random.choice(word_set)])))
print(print_sent(random.choice(table[random.choice(word_set)])))
print(print_sent(random.choice(table[random.choice(word_set)])))
print(print_sent(random.choice(table[random.choice(word_set)])))

    


# TODO: analyze which words can follow other words
# Your code here


# TODO: construct 5 random sentences
# Your code here



# 'exact,': ['had'], 'like': ['her.', 'that?"', 'our', 'to', 'our', 'gauze,', 'a', 'this.'], 'fall.': ['He'], 'King,': ['so', 'rubbing', 'who', 'looking'], '"I\'m': ['going'], 'room,"': ['thought'], 'rest': ['was'], 'led': ['to'], 'because': ['Alice', 'there', 'the', "I've", "there'll"], 'know,': ['I', 'with', 'I', 'unless'], 'next': ['the'], 'turn': ['her'], 'has': ['got'], 'see': ['that', 'the', 'how', 'how', 'through', 'all', 'that', 'a', 'me', 'the', 'me.', 'one', 'what', 'her.', 'if'], 'disgrace.': ['"Really,'], 'leaves': ['are'], 'brown.': ['"Kitty,'], 'too': ['much', 'strong'], 'milk': ['before', 'in', "isn't"], "that's": ['your', 'very'], 'hungry': ['hyaena,'], 'said': ["'Check!'", 'this,', '(in', 'the', 'the', 'afterwards', 'the', 'to'], 'take': ['his'], 'exactly': ['like'], 'forget!"': ['"You'], 'Looking-glass,': ['that'], 'perfectly': ['still:'], 'deny': ['it,'], '"Mind': ['the', 'you'], 'though,"': ['the'], 'wiggling': ['down'], 'Only': ['it'], 'Looking-glass': ['House.', 'House.', 'House,', 'milk', 'House,', 'House!', 'room.'], 'trying': ['to', 'to'], 'fireplace.': ['Oh!'], 'into': ['the', 'the', 'your', 'Looking-glass', 'Looking-glass', 'it,', 'a', 'the', 'a', 'the', 'it--there,'], 'Kitty': ['sat'], 'leave': ['off.', 'the'], 'at': ['the', 'work', 'the', 'the', 'once!', 'last', 'me!"', 'her.', 'last', 'that', 'what', 'last'], 'want': ['so'], 'holding': ['up'], 'drink--But': ['oh,'], 'here,': ['and'], 'wildly': ['up'], 'ashes.': ['She'], 'jumped': ['lightly'], 'memorandum': ['of', 'of'], 'bottle': ['of'], 'through--"': ['She'], 'go': ['and', 'without', 'without', 'the', 'the'], "was--'and": ['if'], 'far': ['rather', 'as', 'better', 'too'], 'Kitty,"': ['Alice'], 'Snowdrop': ['away'], 'Well': ['then,'], 'knocked': ['him'], 'still': ['and', 'a', 'a'], 'one:': ['you'], 'her.': ['Now', '"They', 'So', '"You'], 'asking': ['it'], 'seen': ['from', 'in'], 'Kitty?': ['How', 'I'], 'up!"': ['Alice'], 'words': ['go'], 'saving': ['up'], 'fast,': ['as'], 'next.': ['"It'], 'talking': ['to', 'all', 'more', 'together'], 'be,': ['when'], 'anxiously': ['into'], 'black': ["kitten's", 'kitten'], 'this:': ['first'], 'a': ['corner', 'grand', 'little', 'voice', 'scramble,', 'year?', 'dinner:', 'white', 'nice', 'long', 'hungry', 'bone."', 'dear!"', 'model', 'chair--all', 'fire', 'fire.', 'little', 'way', 'sort', 'bright', 'fire', 'real', 'little', 'little', 'whisper,', 'right', 'little', 'fit,', 'minute', 'little,', 'little', 'little,', 'face', 'little', 'bottle', 'frightened', 'memorandum', 'thinner', 'bit;', 'memorandum', 'book', 'little'], 'about--whenever': ['the'], 'much,': ["I'll"], '"Now,': ['if'], 'lying': ['quite', 'near'], 'hand,': ['and'], "'and": ['there', "I'm"], 'clear': ['that'], 'dress': ['themselves'], "Alice's": ['speech'], 'mischief.': ['The'], 'good': ['directly,"', 'to']