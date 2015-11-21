class StringMatching(object):

    def is_match(self, candidate):
        raise NotImplementedError


class StringContainsAny(StringMatching):

    def __init__(self, *args):
        self.texts = map(str.lower, list(args))

    def is_match(self, candidate):
        return any([text in candidate.lower() for text in self.texts])


class StringContainsAll(StringMatching):

    def __init__(self, *args):
        self.texts = map(str.lower, list(args))

    def is_match(self, candidate):
        return all([text in candidate.lower() for text in self.texts])


class Category(object):

    match_candidates = None

    def belongs_to_category(self, text):
        text = text.lower()
        for match_candidate in self.match_candidates:
            if match_candidate.is_match(text):
                return True
        return False


class Transportation(Category):
    match_candidates = [
            StringContainsAll('Uber technologies inc'),
            StringContainsAll('lyft', 'ride'),
            StringContainsAll('getaround'),
            StringContainsAll('chevron'),
            StringContainsAll('texaco'),
            StringContainsAll('shell oil'),
            StringContainsAll('yosemite oakdale stn'),
            StringContainsAll('yosemite vlg retail'),
            StringContainsAll('boardwalk parking'),
            ]

class EatingOut(Category):
    match_candidates = [
            StringContainsAll('crepe cone'),
            StringContainsAll('garaje'),
            StringContainsAll('philz coffee'),
            StringContainsAll('dusty buns bistro'),
            StringContainsAll('sunrise deli'),
            StringContainsAll('mcdonald'),
            StringContainsAll('mission beach cafe'),
            StringContainsAll('sushirrito'),
            StringContainsAll('kushi tsuru'),
            StringContainsAll('taqueria los coyotes'),
            StringContainsAll('working girls'),
            StringContainsAll('california pizza'),
            StringContainsAll('taco bell'),
            StringContainsAll('the dosa brothers'),
            StringContainsAll('ghirardelli'),
            StringContainsAll('in-n-out'),
            StringContainsAll('the store on the corner'),
            StringContainsAll('starbucks'),
            StringContainsAll('eat24'),
            StringContainsAll('hrd'),
            StringContainsAll('freshroll'),
            StringContainsAll('crepevine'),
            StringContainsAll('sammy\'s on 2nd'),
            StringContainsAll('little skillet'),
            StringContainsAll('pazzia'),
            StringContainsAll('panera bread'),
            StringContainsAll('papalote'),
            StringContainsAll('tin vietnamese'),
            StringContainsAll('boba guys'),
            StringContainsAll('slanted door'),
            StringContainsAll('delancey street'),
            StringContainsAll('ayola'),
            StringContainsAll('the sentinel'),
            StringContainsAll('the chairman'),
            StringContainsAll('cafe madeleine'),
            StringContainsAll('yelpinc'),
            StringContainsAll('tava indian kitchen'),
            StringContainsAll('biere restaurant'),
            StringContainsAll('the house'),
            StringContainsAll('south beach pizza'),
            ]

class Groceries(Category):
    match_candidates = [
            StringContainsAll('safeway store'),
            ]

class Housing(Category):
    match_candidates = [
            ]

class Utilities(Category):
    match_candidates = [
            ]

class Clothing(Category):
    match_candidates = [
            ]

class Leisure(Category):
    match_candidates = [
            StringContainsAll('performance bike shop'),
            StringContainsAll('century theatre'),
            StringContainsAll('big basin redwoods'),
            StringContainsAll('coit tower llc'),
            StringContainsAll('amc metreon'),
            StringContainsAll('zen compound'),
            StringContainsAll('active-network'),
            StringContainsAll('airbnb'),
            StringContainsAll('abv san francisco'),
            ]

class Personal(Category):
    match_candidates = [
            StringContainsAll('t-mobile'),
            StringContainsAll('dogpatch boulders'),
            StringContainsAll('super cuts'),
            StringContainsAll('supercuts'),
            StringContainsAll('carlos shoe repair'),
            ]

class Medical(Category):
    match_candidates = [
            StringContainsAll('camilo riano'),
            StringContainsAll('walgreens'),
            ]

CATEGORIES = [
    Transportation(),
    EatingOut(),
    Groceries(),
    Housing(),
    Utilities(),
    Clothing(),
    Leisure(),
    Personal(),
    Medical(),
]
