from sys import argv

latin_glyphs =  'qwertyuiopasdfghjklzxcvbnmüışğäİö'
orkhon_glyphs = '𐰴𐰙𐰅𐰺𐱃𐰖𐰆𐰄𐰗𐰯𐰀𐰽𐰑𐰊𐰏𐰎𐰳𐰚𐰞𐰔𐰐𐰕𐰋𐰉𐰣𐰢𐰈𐰃𐱁𐰍𐰂𐰄𐰘'
latin_to_orkhon_map = {latin_glyphs[i] : orkhon_glyphs[i] for i in range(len(latin_glyphs))}
def latin_letter_to_orkhon(letter:str) -> str:
    if letter in latin_to_orkhon_map.keys():
        orkhon_letter = latin_to_orkhon_map[letter]
    else:
        orkhon_letter = letter
    return orkhon_letter

word = ' '.join(argv[1:])
newword = ''.join(map(latin_letter_to_orkhon, word))
print(newword)
