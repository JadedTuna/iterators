"""Övningar på iterators."""
import itertools


class Cubes():
    """En iterator som skapar en serie med kuber (i ** 3).

    Talserien utgår från de positiva heltalen: 1, 2, 3, 4, 5, 6, ...
    Talserien som skapas börjar således: 1, 8, 27, 64, 125, 216, ...

    Talserien ska inte ha något slut.

    """
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        cube = self.current ** 3
        self.current += 1
        return cube


class Primes():
    """En iterator som returnerar primtal.

    Talserien som förväntas börjar alltså: 2, 3, 5, 7, 11, 13, 17, 19, 23, ...

    """
    def __init__(self):
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.current += 1
            if Primes.is_prime(self.current):
                return self.current

    @staticmethod
    def is_prime(value):
        for i in range(2, value):
            if value % i == 0:
                return False
        return True


class Fibonacci():
    """En iterator som returnerar de berömda fibonacci-talen.

    Fibonaccis talserie börjar med 0 och 1. Nästa tal är sedan summan av de
    två senaste.

    Alltså börjar serien: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

    """
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        c = self.a
        old_a = self.a
        self.a = self.b
        self.b = old_a + self.b

        return c


class Alphabet():
    """En iterator som returnerar namnen på tecknen i det hebreiska alfabetet.

    Iteratorn returnerar namnen för de hebreiska bokstäverna i alfabetisk
    ordning. Namnen och ordningen är:

    Alef, Bet, Gimel, Dalet, He, Vav, Zayin, Het, Tet, Yod, Kaf, Lamed, Mem,
    Nun, Samekh, Ayin, Pe, Tsadi, Qof, Resh, Shin, Tav

    """
    def __init__(self):
        self.names = ["Alef", "Bet", "Gimel", "Dalet", "He", "Vav", "Zayin",
                      "Het", "Tet", "Yod", "Kaf", "Lamed", "Mem", "Nun",
                      "Samekh", "Ayin", "Pe", "Tsadi", "Qof", "Resh", "Shin",
                      "Tav"]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.names):
            raise StopIteration

        name = self.names[self.index]
        self.index += 1
        return name


class Permutations_IterTools():
    """En iterator som returnerar alla permutationer av en inmatad sträng.

    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """
    def __init__(self, string=""):
        self.permutations = itertools.permutations(string, len(string))

    def __iter__(self):
        return self

    def __next__(self):
        return "".join(next(self.permutations))


class Permutations():
    """En iterator som returnerar alla permutationer av en inmatad sträng.

    Då strängen 'abc' matas in fås: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
    """
    def __init__(self, string=""):
        self.permutations = itertools.permutations(string, len(string))

    def __iter__(self):
        return self

    def __next__(self):
        return "".join(next(self.permutations))


class LookAndSay():
    """En iterator som implementerar look-and-say-talserien.

    Sekvensen fås genom att man läser ut och räknar antalet siffror i
    föregående tal.

    1 läses 'en etta', alltså 11
    11 läses 'två ettor', alltså 21
    21 läses 'en tvåa, en etta', alltså 1211
    1211 läses 'en etta, en tvåa, två ettor', alltså 111221
    111221 läses 'tre ettor, två tvåor, en etta', alltså 312211
    """
    def __init__(self):
        self.last = 1

    def __iter__(self):
        return self

    @staticmethod
    def look_and_say(number):
        chars = str(number)
        num = None
        count = 0
        new_chars = ""
        for char in chars:
            print(char)
            if char == num:
                count += 1
            else:
                if num is not None:
                    new_chars += str(count) + str(num)
                num = char
                count = 1

        if count:
            new_chars += str(count) + str(num)

        return int(new_chars)

    def __next__(self):
        saved = self.last
        self.last = self.look_and_say(self.last)
        return saved
