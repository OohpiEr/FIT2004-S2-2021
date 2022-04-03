""" Test cases for Question 3 of FIT2004 Assignment """

__author__ = "Arthur Lee"

import unittest
from assignment1 import interest_groups


class TestInterestGroups(unittest.TestCase):
    def test1(self):
        """ Provided in Assignment Specifications """
        data = [("nuka", ["birds", "napping"]),
                ("hadley", ["napping birds", "nash equilibria"]),
                ("yaffe", ["rainy evenings", "the colour red", "birds"]),
                ("laurie", ["napping", "birds"]),
                ("kamalani", ["birds", "rainy evenings", "the colour red"])]

        expected = sorted([["laurie", "nuka"], ["hadley"], ["kamalani", "yaffe"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    # def test2(self):
    #     """ Empty List """
    #     data = []

    #     expected = sorted([])

    #     raw_actual = interest_groups(data)
    #     actual = sorted(raw_actual)

    #     self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test3(self):
        """ All same single interest """
        data = [("john", ["coding"]),
                ("arthur", ["coding"]),
                ("jacky", ["coding"]),
                ("zach", ["coding"]),
                ("laura", ["coding"]),
                ("desmond", ["coding"]),
                ("benny", ["coding"]),
                ("casper", ["coding"])]

        expected = sorted([sorted(["john", "arthur", "jacky", "zach", "laura", "desmond", "benny", "casper"])])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test4(self):
        """ All same multiple interests sorted """
        data = [("timothy", ["jogging", "gaming", "fishing"]),
                ("jimmy", ["jogging", "gaming", "fishing"]),
                ("arthur", ["jogging", "gaming", "fishing"]),
                ("zim", ["jogging", "gaming", "fishing"]),
                ("lauren", ["jogging", "gaming", "fishing"]),
                ("yanny", ["jogging", "gaming", "fishing"]),
                ("benjamin", ["jogging", "gaming", "fishing"]),
                ("ethan", ["jogging", "gaming", "fishing"]),
                ("nate", ["jogging", "gaming", "fishing"])]

        expected = sorted([sorted(["timothy", "jimmy", "arthur", "zim", "lauren", "yanny", "benjamin", "ethan", "nate"])])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test5(self):
        """ All same multiple interests not sorted """
        data = [("timothy", ["jogging", "gaming", "fishing"]),
                ("jimmy", ["gaming", "jogging", "fishing"]),
                ("arthur", ["fishing", "gaming", "jogging"]),
                ("zim", ["jogging", "gaming", "fishing"]),
                ("lauren", ["jogging", "gaming", "fishing"]),
                ("yanny", ["jogging", "gaming", "fishing"]),
                ("benjamin", ["gaming", "fishing", "jogging"]),
                ("ethan", ["jogging", "fishing", "gaming"]),
                ("nate", ["fishing", "jogging", "gaming"])]

        expected = sorted([sorted(["timothy", "jimmy", "arthur", "zim", "lauren", "yanny", "benjamin", "ethan", "nate"])])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test6(self):
        """ All different single interest """
        data = [("jack", ["coding"]),
                ("nathan", ["teaching computer science"]),
                ("ian", ["educating students on algorithms and data structures"]),
                ("arthur", ["programming stuff"]),
                ("doris", ["chilling"]),
                ("timmy", ["feeding pigeons"]),
                ("aj", ["playing games"]),
                ("dawn", ["catching pokemon"]),
                ("light", ["killing people with a death note"])]

        expected = sorted([["jack"], ["nathan"], ["ian"], ["arthur"], ["doris"], ["timmy"], ["aj"], ["dawn"], ["light"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test7(self):
        """ All different multiple interests """
        data = [("arthur", ["coding", "playing video games", "math", "binging youtube"]),
                ("ash", ["becoming the greatest pokemon master of all time"]),
                ("ian", ["roasting other units", "teaching computer science"]),
                ("phoenix", ["legal assistance", "bluffing his way to victory"]),
                ("barbara", ["singing", "dancing", "becoming an idol"])]

        expected = sorted([["arthur"], ["ash"], ["ian"], ["phoenix"], ["barbara"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test8(self):
        """ If two different interest lists concatenate to the same string """
        data = [("arthur", ["car", "racing"]),
                ("jacky", ["carracing"])]

        expected = sorted([["arthur"], ["jacky"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test9(self):
        """ Only one person """
        data = [("arthur", ["coding", "math"])]

        expected = sorted([["arthur"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test10(self):
        """ Random example """
        data = [("tony", ["rich", "billionaire", "superhero"]),
                ("bruce", ["superhero", "rich", "billionaire"]),
                ("nolan", ["look at what they need to mimic a fraction of our power", "think mark think", "thats the neat part you dont"]),
                ("peter", ["superhero"]),
                ("steve", ["from another time", "superhero"])]

        expected = sorted([sorted(["tony", "bruce"]), ["steve"], ["nolan"], ["peter"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test11(self):
        """ Random example """
        data = [("jack", ["clash of clans", "clash royale"]),
                ("ian", ["apex legends", "dota two"]),
                ("arthur", ["genshin impact", "pokemon"]),
                ("desmond", ["pokemon", "genshin impact"]),
                ("nick", ["clash royale", "clash of clans"]),
                ("zachary", ["genshin impact", "honkai impact third", "apex legends"]),
                ("elaine", ["tears of themis", "ddlc"]),
                ("steve", ["cuphead", "undertale", "fortnite", "clash of clans"]),
                ("john", ["clash royale", "clash of clans"]),
                ("tim", ["genshin impact", "pokemon"]),
                ("dan", ["genshin impact", "pokemon"]),
                ("ronald", ["undertale", "cuphead", "clash of clans", "fortnite"]),
                ("daniel", ["pokemon", "genshin impact"])]

        expected = sorted([sorted(["jack", "nick", "john"]), ["ian"], sorted(["arthur", "desmond", "tim", "dan", "daniel"]), ["zachary"], ["elaine"], sorted(["steve", "ronald"])])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test12(self):
        """ There is one imposter among us """
        data = [("john", ["coding", "math"]),
                ("arthur", ["math", "coding"]),
                ("nick", ["math", "coding"]),
                ("ian", ["teaching computer science", "roasting other units"]),
                ("dave", ["math", "coding"])]

        expected = sorted([sorted(["john", "arthur", "nick", "dave"]), ["ian"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test13(self):
        """ All interests are pure spaces (Not sure if counts as empty string, but better to be safe than sorry) """
        data = [("arthur", ["   ", " "]),
                ("ethan", ["                       "]),
                ("dave", [" ", " ", " ", " ", " ", " "]),
                ("nathan", [" ", "      "]),
                ("apple", [" ", "   "]),
                ("ian", ["    "])]

        expected = sorted([sorted(["arthur", "apple"]), ["ethan"], ["dave"], ["nathan"], ["ian"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test14(self):
        """ Some interests are pure spaces (Better to be safe than sorry) """
        data = [("jimmy", ["   ", " "]),
                ("david", ["math", "                       ", "a    lie"]),
                ("nicki", [" "]),
                ("arthur", ["st u ff", "                                          ", " ", " ", " "]),
                ("ian", [" ", "   "]),
                ("apple", ["    "])]

        expected = sorted([sorted(["jimmy", "ian"]), ["david"], ["nicki"], ["arthur"], ["apple"]])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))

    def test15(self):
        data = [('arthur', ['ayaka', 'is', 'motivation']),
                ('jimmy', ['aya', 'kais', 'motivation']),
                ('zach', ['ayaka', 'is', 'motivation']),
                ('brian', ['aya', 'kais', 'motivation']),
                ('timmy', ['ayaka', 'is', 'motivation']),
                ('hutao', ['aya', 'kais', 'motivation'])]

        expected = sorted([sorted(["arthur", "zach", "timmy"]), sorted(["jimmy", "brian", "hutao"])])

        raw_actual = interest_groups(data)
        actual = sorted(raw_actual)

        self.assertEqual(expected, actual, msg="Raw Actual: " + str(raw_actual))


if __name__ == '__main__':
    unittest.main()
