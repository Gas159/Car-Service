"""
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""


def generate_hashtag(s):
    # res  = '#'+s.title().replace(' ','')
    res = "#" + "".join(i.capitalize() for i in s.split())
    return False if len(res) > 140 or len(s) == 0 else res


print(generate_hashtag(" Hello there thanks for trying my Kata"))
