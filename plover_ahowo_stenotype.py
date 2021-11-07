from plover.system.english_stenotype import *

# ahowo steno

#   | ə p t w     f t S l i |  ~>  | # X p t w     f t S l i |
#   | s b d r  *  n d g z ə |  ~>  | # s b d r  *  n d g z x |
#   |                       |  ~>  | #                       |
#   |      a e   ɪ ʊ        |  ~>  | #      a e   I U        |

# vowels:
# a -> a, æ, ɑ, ʌ -> short a as in *a*h, *a*ct, *a*fter
# o -> o, ɔ -> as in *o*pposite, *o*dd, *o*f, *o*ff
# e -> e -> as in *eh*, *ai*d, h*a*te, w*ay*
# u -> u, ɯ -> as in *u*psilon, *oo*ps, h*u*ge
# eu -> i -> as in h*e*, b*e*, b*ee*, f*ee*, l*ea*d
# ou -> ou (dipthong) -> as in c*oa*t, *oa*t, *o*de
# au -> au (dipthong) -> as in ab*ou*t, h*ow*, p*ow*er
# aeu -> ai (dipthong) -> as in h*i*, b*ye*, h*igh*, b*i*te
# oeu -> oi (dipthong) -> as in b*oy*, p*oi*sed, ll*oy*d
# oe -> ɛ, œ -> as in *e*dit, *e*xcellent, *e*bb
# ae -> ɪ -> as in sp*i*n, *i*f, h*i*s
# X/[nothing] -> ə -> as in *u*pon, *uh*, c*oul*d

# consonants:
#
# LH consonants:
# tp- -> f-
# tk- -> d-
# ph- -> m-
# tph- -> n-
# hr- -> l-
# skwr- -> j-
# tkpw- -> v-
# wr- -> y-
# kh- -> ch-
# sh- -> sh-
# th- -> th-
# stp- -> z-
# kwr- -> g-
# pw- -> b-
#
# RH consonants
# -pb -> -n
# -pl -> -m
# -z -> -s
# -g -> -ing (sometimes)
# -bg -> -k
# -j -> -sh
# -jt -> -ch
# -jd -> -j (as in *j* u *dge*)
# -td -> -th
# -f -> -f or -s or -z
# -fb -> -v
#

# Inversions allowed:
# one inversion for -r (a la TP-FRT for first, while it's technically "fifrt" or "fisrt")
#


KEYS = (
    "#",
    "s-",
    "x-",
    "t-",
    "k-",
    "p-",
    "w-",
    "h-",
    "r-",
    "a-",
    "o-",
    "*",
    "-e",
    "-u",
    "-f",
    "-r",
    "-p",
    "-b",
    "-l",
    "-g",
    "-t",
    "-d",
    "-j",
    "-z",
)

KEYMAPS = {
    "Keyboard": {
        # Number bar
        "#": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
        # left-hand consonants      #  1  2  3  4
        "s-": ["q"],
        "x-": ["a"],  #  s  t  p  h
        "t-": ["w"],
        "k-": ["s"],  #  x  k  w  r
        "p-": ["e"],
        "w-": ["d"],
        "h-": ["r"],
        "r-": ["f"],
        # left-hand vowels          #  5  0
        "a-": ["c"],
        "o-": ["v"],  #  a  o
        # undo key                  #  *
        "*": ["t", "g", "y", "h"],
        # right-hand vowels         #  e u
        "-e": ["n"],
        "-u": ["m"],
        # right-hand consonants     #  6  7  8  9
        "-f": ["u"],
        "-r": ["j"],  #  f  p  g  t  j
        "-p": ["i"],
        "-b": ["k"],  #  r  b  l  d  z
        "-l": ["o"],
        "-g": ["l"],
        "-t": ["p"],
        "-j": [
            "["
        ],  # j and d are swapped despite being out of steno order; d is just a much more frequent key
        "-d": [";"],
        "-z": ["'"],
        # other
        "arpeggiate": ["space"],
        "no-op": ["z", "x", "b", ",", ".", "/", "]", "\\"],
    }
}

NUMBERS = {
    "s-": "1-",
    "t-": "2-",
    "p-": "3-",
    "h-": "4-",
    "a-": "5-",
    "o-": "0-",
    "-f": "-6",
    "-p": "-7",
    "-l": "-8",
    "-t": "-9",
}


ORTHOGRAPHY_RULES = [
    # dropping silent e before endings
    (
        r"^(.+[bcdfghjklmnpqrstuvz])e \^ (able|age|ed|est|ing|ings|ion|ory|ous)$",
        r"\1\2",
    ),
    # dropping e after double vowels
    (r"^(.+[ie])e \^ (e.+)$", r"\1\2"),
    # consonant + y pluralization
    # (r'^(.+[bcdfghjklmnpqrstvwxz])y \^ s$', r'\1ies'),
    # consonant doubling
    (
        r"^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ ((ee|[eo]i)(?:[bcdfghjklmnpqrstvwxyz].?)?)$",
        r"\1\2\2\3",
    ),
    (
        r"^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (([aeiouy]|[ai]e)(?:[bcdfghjklmnpqrstvwxyz].?))$",
        r"\1\2\2\3",
    ),
    (
        r"^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ ([ei]?ous)$",
        r"\1\2\2\3",
    ),
    (
        r"^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ ([ai]ble)$",
        r"\1\2\2\3",
    ),
    (
        r"^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ ([ae]nce)$",
        r"\1\2\2\3",
    ),
    (
        r"^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (e[rn]ing)$",
        r"\1\2\2\3",
    ),
    (
        r"^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (ation)$",
        r"\1\2\2\3",
    ),
    (
        r"^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (iness)$",
        r"\1\2\2\3",
    ),
    (
        r"^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (ably)$",
        r"\1\2\2\3",
    ),
    (
        r"^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (ened)$",
        r"\1\2\2\3",
    ),
    (
        r"^(.*(?:[bcdfghjklmnprstvwxyz]|qu)[aeiou])([bcdfgklmnprtvz]) \^ (ings)$",
        r"\1\2\2\3",
    ),
    # == +ly ==
    # artistic + ly = artistically
    (r"^(.*[aeiou]c) \^ ly$", r"\1ally"),
    # == +ry ==
    # statute + ry = statutory
    (r"^(.*t)e \^ ry$", r"\1ory"),
    # == t +cy ==
    # frequent + cy = frequency (tcy/tecy removal)
    (r"^(.*[naeiou])te? \^ cy$", r"\1cy"),
    # == +s ==
    # establish + s = establishes (sibilant pluralisation)
    (r"^(.*(?:s|sh|x|z|zh)) \^ s$", r"\1es"),
    # speech + s = speeches (soft ch pluralisation)
    (r"^(.*(?:oa|ea|i|ee|oo|au|ou|l|n|(?<![gin]a)r|t)ch) \^ s$", r"\1es"),
    # cherry + s = cherries (consonant + y pluralisation)
    (r"^(.+[bcdfghjklmnpqrstvwxz])y \^ s$", r"\1ies"),
    # == y ==
    # die+ing = dying
    (r"^(.+)ie \^ ing$", r"\1ying"),
    # metallurgy + ist = metallurgist
    (r"^(.+[cdfghlmnpr])y \^ ist$", r"\1ist"),
    # beauty + ful = beautiful (y -> i)
    (r"^(.+[bcdfghjklmnpqrstvwxz])y \^ ([a-hj-xz].*)$", r"\1i\2"),
]


ORTHOGRAPHY_RULES_ALIASES = {
    "able": "ible",
    "ability": "ibility",
}

SUFFIX_KEYS = ("-f", "-r", "-p", "-b", "-l", "-g", "-t", "-j", "-d", "-z")
IMPLICIT_HYPHEN_KEYS = ("a-", "o-", "-e", "-u", "*")

ORTHOGRAPHY_WORDLIST = "american_english_words.txt"
DICTIONARIES_ROOT = "asset:plover:assets"
DEFAULT_DICTIONARIES = ()
