#Name: Sam Dunning
#Student Number: 121404894
import random
import ast
import time

class study:
    def __init__(self):
        #Hirigana lists - Both the Hirigana symbols and the English sound of each Hirigana
        self._hirigana1 = [b'\xe3\x81\x82',b'\xe3\x81\x84',b'\xe3\x81\x86',b'\xe3\x81\x88',b'\xe3\x81\x8a',b'\xe3\x81\x8b',b'\xe3\x81\x8c',b'\xe3\x81\x8d',b'\xe3\x81\x8e',b'\xe3\x81\x8f',b'\xe3\x81\x90',b'\xe3\x81\x91',b'\xe3\x81\x92',b'\xe3\x81\x93',b'\xe3\x81\x94',b'\xe3\x81\x95',b'\xe3\x81\x96',b'\xe3\x81\x97',b'\xe3\x81\x98',b'\xe3\x81\x99',b'\xe3\x81\x9a',b'\xe3\x81\x9b',b'\xe3\x81\x9c',b'\xe3\x81\x9d',b'\xe3\x81\x9e',b'\xe3\x81\x9f',b'\xe3\x81\xa0',b'\xe3\x81\xa1',b'\xe3\x81\xa2',b'\xe3\x81\xa3',b'\xe3\x81\xa4',b'\xe3\x81\xa5',b'\xe3\x81\xa6',b'\xe3\x81\xa7',b'\xe3\x81\xa8',b'\xe3\x81\xa9',b'\xe3\x81\xaa',b'\xe3\x81\xab',b'\xe3\x81\xac',b'\xe3\x81\xad',b'\xe3\x81\xae',b'\xe3\x81\xaf',b'\xe3\x81\xb0',b'\xe3\x81\xb2',b'\xe3\x81\xb3',b'\xe3\x81\xb4',b'\xe3\x81\xb5',b'\xe3\x81\xb6',b'\xe3\x81\xb7',b'\xe3\x81\xb8',b'\xe3\x81\xb9',b'\xe3\x81\xba',b'\xe3\x81\xbb',b'\xe3\x81\xbc',b'\xe3\x81\xbd',b'\xe3\x81\xbe',b'\xe3\x81\xbf',b'\xe3\x82\x80',b'\xe3\x82\x81',b'\xe3\x82\x82',b'\xe3\x82\x83',b'\xe3\x82\x84',b'\xe3\x82\x85',b'\xe3\x82\x86',b'\xe3\x82\x87',b'\xe3\x82\x88',b'\xe3\x82\x89',b'\xe3\x82\x8a',b'\xe3\x82\x8b',b'\xe3\x82\x8c',b'\xe3\x82\x8d',b'\xe3\x82\x92',b'\xe3\x82\x93',b'\xe3\x82\x8f']
        self._hirigana2 = ["a","i","u","e","o","ka","ga","ki","gi","ku","gu","ke","ge","ko","go","sa","za","shi","ji","su","zu","se","ze","so","zo","ta","da","chi","ji","0","tsu","dzu","te","de","to","do","na","ni","nu","ne","no","ha","da","hi","bi","pi","fu","bu","pu","he","be","pe","ho","bo","po","ma","mi","mu","me","mo","1","ya","2","yu","3","yo","ra","ri","ru","re","ro","wo","n","wa"]
        
        #Katakana lists - Both the Katakana symbols and the English sound of each Katakana
        self._katakana1 = [b'\xe3\x82\xa2', b'\xe3\x82\xa4', b'\xe3\x82\xa6', b'\xe3\x82\xa8', b'\xe3\x82\xaa', b'\xe3\x82\xab', b'\xe3\x82\xac', b'\xe3\x82\xad', b'\xe3\x82\xae', b'\xe3\x82\xaf', b'\xe3\x82\xb0', b'\xe3\x82\xb1', b'\xe3\x82\xb2', b'\xe3\x82\xb3', b'\xe3\x82\xb4', b'\xe3\x82\xb5', b'\xe3\x82\xb6', b'\xe3\x82\xb7', b'\xe3\x82\xb8', b'\xe3\x82\xb9', b'\xe3\x82\xba', b'\xe3\x82\xbb', b'\xe3\x82\xbc', b'\xe3\x82\xbd', b'\xe3\x82\xbe', b'\xe3\x82\xbf', b'\xe3\x83\x80', b'\xe3\x83\x81', b'\xe3\x83\x82', b'\xe3\x83\x83', b'\xe3\x83\x84', b'\xe3\x83\x85', b'\xe3\x83\x86', b'\xe3\x83\x87', b'\xe3\x83\x88', b'\xe3\x83\x89', b'\xe3\x83\x8a', b'\xe3\x83\x8b', b'\xe3\x83\x8c', b'\xe3\x83\x8d', b'\xe3\x83\x8e', b'\xe3\x83\x8f', b'\xe3\x83\x90', b'\xe3\x83\x92', b'\xe3\x83\x93', b'\xe3\x83\x94', b'\xe3\x83\x95', b'\xe3\x83\x96', b'\xe3\x83\x97', b'\xe3\x83\x98', b'\xe3\x83\x99', b'\xe3\x83\x9a', b'\xe3\x83\x9b', b'\xe3\x83\x9c', b'\xe3\x83\x9d', b'\xe3\x83\x9e', b'\xe3\x83\x9f', b'\xe3\x83\xa0', b'\xe3\x83\xa1', b'\xe3\x83\xa2', b'\xe3\x83\xa3', b'\xe3\x83\xa4', b'\xe3\x83\xa5', b'\xe3\x83\xa6', b'\xe3\x83\xa7', b'\xe3\x83\xa8', b'\xe3\x83\xa9', b'\xe3\x83\xaa', b'\xe3\x83\xab', b'\xe3\x83\xac', b'\xe3\x83\xad', b'\xe3\x83\xb2', b'\xe3\x83\xb3', b'\xe3\x83\xaf']
        self._katakana2 = ["a","i","u","e","o","ka","ga","ki","gi","ku","gu","ke","ge","ko","go","sa","za","shi","ji","su","zu","se","ze","so","zo","ta","da","chi","ji","0","tsu","dzu","te","de","to","do","na","ni","nu","ne","no","ha","da","hi","bi","pi","fu","bu","pu","he","be","pe","ho","bo","po","ma","mi","mu","me","mo","1","ya","2","yu","3","yo","ra","ri","ru","re","ro","wo","n","wa"]
        
        #Kanji lists - Base Set of Intial Kanji to Learn
        self._kanji1 = [b'\xe6\x97\xa5', b'\xe4\xb8\x80', b'\xe5\xa4\xa7', b'\xe5\xb9\xb4', b'\xe4\xb8\xad', b'\xe4\xbc\x9a', b'\xe4\xba\xba', b'\xe6\x9c\xac', b'\xe6\x9c\x88', b'\xe9\x95\xb7', b'\xe5\x9b\xbd', b'\xe5\x87\xba', b'\xe4\xb8\x8a', b'\xe5\x8d\x81', b'\xe7\x94\x9f', b'\xe5\xad\x90', b'\xe5\x88\x86', b'\xe6\x9d\xb1', b'\xe4\xb8\x89', b'\xe8\xa1\x8c', b'\xe5\x90\x8c', b'\xe4\xbb\x8a', b'\xe9\xab\x98', b'\xe9\x87\x91', b'\xe6\x99\x82', b'\xe6\x89\x8b', b'\xe8\xa6\x8b', b'\xe5\xb8\x82', b'\xe5\x8a\x9b', b'\xe7\xb1\xb3', b'\xe8\x87\xaa', b'\xe5\x89\x8d', b'\xe5\x86\x86', b'\xe5\x90\x88', b'\xe7\xab\x8b', b'\xe5\x86\x85', b'\xe4\xba\x8c', b'\xe4\xba\x8b', b'\xe7\xa4\xbe', b'\xe8\x80\x85', b'\xe5\x9c\xb0', b'\xe4\xba\xac', b'\xe9\x96\x93', b'\xe7\x94\xb0', b'\xe4\xbd\x93', b'\xe5\xad\xa6', b'\xe4\xb8\x8b', b'\xe7\x9b\xae', b'\xe4\xba\x94', b'\xe5\xbe\x8c', b'\xe6\x96\xb0', b'\xe6\x98\x8e', b'\xe6\x96\xb9', b'\xe9\x83\xa8', b'. ', b'\xe5\x85\xab', b'\xe5\xbf\x83', b'\xe5\x9b\x9b', b'\xe6\xb0\x91', b'\xe5\xaf\xbe', b'\xe4\xb8\xbb', b'\xe6\xad\xa3', b'\xe4\xbb\xa3', b'\xe8\xa8\x80', b'\xe4\xb9\x9d', b'\xe5\xb0\x8f', b'\xe6\x80\x9d', b'\xe4\xb8\x83', b'\xe5\xb1\xb1', b'\xe5\xae\x9f', b'\xe5\x85\xa5', b'\xe5\x9b\x9e', b'\xe5\xa0\xb4', b'\xe9\x87\x8e', b'\xe9\x96\x8b', b'\xe4\xb8\x87', b'\xe5\x85\xa8', b'\xe5\xae\x9a', b'\xe5\xae\xb6', b'\xe5\x8c\x97', b'\xe5\x85\xad', b'\xe5\x95\x8f', b'\xe8\xa9\xb1', b'\xe6\x96\x87', b'\xe5\x8b\x95', b'\xe5\xba\xa6', b'\xe7\x9c\x8c', b'\xe6\xb0\xb4', b'\xe5\xae\x89', b'\xe6\xb0\x8f', b'\xe5\x92\x8c', b'\xe6\x94\xbf', b'\xe4\xbf\x9d', b'\xe8\xa1\xa8', b'\xe9\x81\x93', b'\xe7\x9b\xb8', b'\xe6\x84\x8f', b'\xe7\x99\xba', b'\xe4\xb8\x8d', b'\xe5\x85\x9a']
        self._kanji2 = ['sun', 'one', 'big', 'year', 'middle', 'to meet', 'human being, people', 'book', 'moon, month', 'long', 'country', 'to go out', 'up, top', '10', 'life', 'child', 'minute', 'east', 'three', 'to go', 'same', 'now', 'high, expensive', 'money, gold', 'time', 'hand', 'to see, to look', 'city', 'power', 'rice', 'oneself', 'before', 'yen (Japanese currency)', 'to combine', 'to stand', 'inside', 'two', 'affair, matter', 'company, society', 'person', 'ground, place', 'capital', 'interval, between', 'rice field', 'body', 'to study', 'down, under', 'eye', 'five', 'after', 'new', 'bright, clear', 'direction', 'section', 'woman', 'eight', 'heart', 'four', 'people, nation', 'opposite', 'main, master', 'right, correct', 'to substitute, generation', 'to say', 'nine', 'small', 'to think', 'seven', 'mountain', 'real', 'to enter', 'to turn around, time', 'place', 'field', 'to open', '10,000', 'whole', 'to fix', 'house', 'north', 'six', 'question', 'to speak', 'letter, writings', 'to move', 'degree, time', 'prefecture', 'water', 'inexpensive, peaceful', 'courtesy name (Mr., Mrs.)', 'harmonious, peace', 'government, politics', 'to maintain, to keep', 'to express, surface', 'way', 'phase, mutual', 'mind, meaning', 'to start, to emit', 'not, un-, in-', 'political party']
        


        #Example Sentences with both hirigana and romanji to use later
        self.__sentencehiri = ["おはようございます","げんきですか","すみません"]
        self.__sentenceromanji = ["gomen nasai","watashi wa nihongo ga sukoshi shika hanasemasen"]

        #Code to show lists of hirigana and romanji next to each other for testing
        # for i in range(len(self._kanji1)):
        #     print(self._kanji1[i].decode("utf-8"), self._kanji2[i])
        # print(len(self._kanji1),len(self._kanji2))

    def hirigana(self):
        #This is a method to review all of the stored Hirigana. You are tested on all and Told if right or wrong.
        #Iterating through list of Hirigana
        for i in range(len(self._hirigana1)):
            #randomizing Selection
            r = random.randint(0,len(self._hirigana1)-1)
            #Testing you on each character
            if self._hirigana2[r] != 0 and self._hirigana2[r] != 1 and self._hirigana2[r] != 2 and self._hirigana2[r] != 3:
                print("What does "+ self._hirigana1[r].decode("utf-8") + "sound like?")
                ans = input("Ans: ")
                #Break Loop if want to leave
                if ans == "leave":
                    return 1
                #Correct or Wrong!
                if ans == self._hirigana2[r]:
                    print("Correct!!")
                else:
                    print("Incorrect ; (" + "It sounds like : " + self._hirigana2[r])
        print("Whole Hirigana review complete!")
        return self._hirigana1
    #Method to Review Katakana - Another set of Japanese Characters - Did not get to this
    def katakana(self):
        #This is a method to review all of the stored Katakana. You are tested on all and Told if right or wrong.
        #Iterating through list of Katakana
        for i in range(len(self._katakana1)):
            #randomizing Selection
            r = random.randint(0,len(self._katakana1)-1)
            #Testing you on each character
            if self._katakana2[r] != 0 and self._katakana2[r] != 1 and self._katakana2[r] != 2 and self._katakana2[r] != 3:
                print("What does "+ self._katakana1[r].decode("utf-8") + "sound like?")
                ans = input("Ans: ")
                #Break Loop if want to leave
                if ans == "leave":
                    return 1
                #Correct or Wrong!
                if ans == self._katakana2[r]:
                    print("Correct!!")
                else:
                    print("Incorrect ; (" + "It sounds like : " + self._katakana2[r])
        print("Whole Katakana review complete!")
        return self._katakana1

    #Method to Review Kanji - The main set of Japanese Characters
    def kanji(self):
    #This is a method to review all of the stored Kanji. You are tested on all and Told if right or wrong.
        #Iterating through list of Kanji
        for i in range(len(self._kanji1)):
            #randomizing Selection
            r = random.randint(0,len(self._kanji1)-1)
            #Testing you on each character
            if self._kanji2[r] != 0 and self._kanji2[r] != 1 and self._kanji2[r] != 2 and self._kanji2[r] != 3:
                print("What does this Kanji mean?: "+ self._kanji1[r].decode("utf-8"))
                ans = input("Ready to reveal the answer?: \n")
                #Break Loop if want to leave
                if ans == "leave":
                    return 1
                #Correct or Wrong!
                print("This Kanji means: " + self._kanji2[r])
        print("Whole Kanji review complete!")
        return self._kanji1
    

    #This method lets you input or use a sentence in Hirigana and translates for you after you have tried Translating
    def hiriSentenceTest(self):
        print("Test Sentences: \n")
        for i in self.__sentencehiri:
            print("Sentence: ")
            print("Translate - " + i)
            ans = input("Press 'Y' to reveal the Answer: ")
            #Break Loop if want to leave
            if ans == "leave":
                return 1
            print("Romanji - "+ str(translate.hiriganaTranslate(self,i)))
        return 1
    # Same thing for Katakana characters
    def kataSentenceTest(self):
        print("Test Sentences: \n")
        for i in self.__sentencehiri:
            print("Sentence: ")
            print("Translate - " + i)
            ans = input("Press 'Y' to reveal the Answer: ")
            #Break Loop if want to leave
            if ans == "leave":
                return 1
            print("Romanji - "+ str(translate.hiriganaTranslate(self,i)))
        return 1 



class daily(study):
    #Initializing all set of daily characters to learn
    def __init__(self):
        super().__init__()
        #Opening all files to be edited
        self.__hir = open("C://Users//samdd//Dropbox//2ndYear//Python&C++//Intermediate_Programming//CAJapanese//hiriganaDaily.txt", "+r")
        self.__kat = open("C://Users//samdd//Dropbox//2ndYear//Python&C++//Intermediate_Programming//CAJapanese//katakanaDaily.txt", "+r")
        self.__kanj = open("C://Users//samdd//Dropbox//2ndYear//Python&C++//Intermediate_Programming//CAJapanese//kanjiDaily.txt", "+r")

    # This is a daily small set of Hirigana characters to do everyday
    def dailyhirigana(self):
        #Reading data from file
        undone1,doing1,done1 = self.__hir.readlines()
        try:    # Breaking down data into Learnt, Learning and Unlearned
            undone = undone1.split(","); undone[-1] = undone[-1][:-1]
            doing = doing1.split(","); doing[-1] = doing[-1][:-1]
            done = done1.split(","); done[-1] = done[-1][:-13]
        except:
            print("Invalid Data Added to text file. ;(")
            return
        #learning Process - Iterates through learning characters. And tests you.
        for i in doing:
            print("What is this hirigana?: " + self._hirigana1[self._hirigana2.index(i)].decode("utf-8"))
            ans = input("Is this 1.Easy 2.Ok 3.Hard to recall? (1/2/3)\n")
            if ans == "1":
                #Changing learned Characters
                doing.remove(i)
                done.append(i)
        doing.append(undone[:5])
        self.__hir.close()
        
        # Changing the characters you have learned and ones you havent in file
        self.__hir = open("C://Users//samdd//Dropbox//2ndYear//Python&C++//Intermediate_Programming//CAJapanese//hiriganaDaily.txt", "+w")
        
        self.__hir.write("[")
        for i in range(len(undone)):
            if undone[i] == undone[-1]:
                self.__hir.write('"' + str(undone[i]) + "]")
            else:
                self.__hir.write('"' + str(undone[i]) + '",')
        self.__hir.write("\n")

        self.__hir.write("[")
        for i in range(len(doing)):
            if doing[i] == doing[-1]:
                self.__hir.write('"' + str(doing[i]) + "]")
            else:
                self.__hir.write('"' + str(doing[i]) + '",')
        self.__hir.write("\n")

        self.__hir.write("[")
        for i in range(len(done)):
            if done[i] == done[-1]:
                self.__hir.write('"' + str(done[i]) + "]")
            else:
                self.__hir.write('"' + str(done[i]) + '",')

        self.__hir.close()
        return 1
    
    #Same thing for Katakana 
    def dailykatakana(self):
        undone1,doing1,done1 = self.__kat.readlines()
        try:
            undone = undone1.split(","); undone[-1] = undone[-1][:-1]
            doing = doing1.split(","); doing[-1] = doing[-1][:-1]
            done = done1.split(","); done[-1] = done[-1][:-13]
        except:
            print("Invalid Data Added to text file. ;(")
            return
        for i in doing:
            print("What is this hirigana?: " + self._katakana1[self._katakana2.index(i)].decode("utf-8"))
            ans = input("Is this 1.Easy 2.Ok 3.Hard to recall? (1/2/3)\n")
            if ans == "1":
                doing.remove(i)
                done.append(i)
        doing.append(undone[:5])
        self.__kat.close()
        
        self.__kat = open("C://Users//samdd//Dropbox//2ndYear//Python&C++//Intermediate_Programming//CAJapanese//hiriganaDaily.txt", "+w")
        
        self.__kat.write("[")
        for i in range(len(undone)):
            if undone[i] == undone[-1]:
                self.__kat.write('"' + str(undone[i]) + "]")
            else:
                self.__kat.write('"' + str(undone[i]) + '",')
        self.__kat.write("\n")

        self.__kat.write("[")
        for i in range(len(doing)):
            if doing[i] == doing[-1]:
                self.__kat.write('"' + str(doing[i]) + "]")
            else:
                self.__kat.write('"' + str(doing[i]) + '",')
        self.__kat.write("\n")

        self.__kat.write("[")
        for i in range(len(done)):
            if done[i] == done[-1]:
                self.__kat.write('"' + str(done[i]) + "]")
            else:
                self.__kat.write('"' + str(done[i]) + '",')

        self.__hir.close()
        return 1


class translate(study):
    def __init__(self):
        super().__init__()

        #Example Translation Sentences
        self.__sentencehiri = ["おはようございます","げんきですか","すみません"]
        self.__sentenceromanji = ["gomen nasai","watashi wa nihongo ga sukoshi shika hanasemasen"]

    #This is the example translaiton method. It gives some examples of sentence translations
    def exampleTranslate(self):
        print("This is a function showing three sentence translations: ")
        print(self.__sentencehiri)
        #Translate the Hirigana Sentences
        for i in self.__sentencehiri:
            #Hirigana Translations
            print("Sentence:")
            print("Hirigana - " + i)
            print("Romanji - "+ str(self.hiriganaTranslate(i)))
            print("\n")

        #Translate the Romanji Sentences
        for i in self.__sentenceromanji:
            #Romanji Translations
            print("Sentence:")
            print("Romanji - " + i)
            print("Hirigana - " + str(self.romanjiTranslate(i)))
            print("\n")
        return 1

    #This is the method that translates from Hirigana to Romanji for you
    def hiriganaTranslate(self,input):
        s = list(input)
        trans = ""
        #Here all of the grammer rules had to be accounted for and the characters also encoded with thier Unicode values
        for i in s:
            trans += self._hirigana2[self._hirigana1.index(i.encode("utf-8"))]
            #Grammer Rule 1: When っ appears, it doesnt make a sound. It only adds the last letter of the last Hirgana again.
            if self._hirigana2[self._hirigana1.index(i.encode("utf-8"))] == "0":
                trans = trans[:-1]
                trans += trans[-1]
            #Grammer Rule 2: This is when a small ゃ appears
            if self._hirigana2[self._hirigana1.index(i.encode("utf-8"))] == "1":
                trans = trans[:-2]
                trans += "ya"
            #Grammer Rule 3: This is when a small ゅ appears
            if self._hirigana2[self._hirigana1.index(i.encode("utf-8"))] == "2":
                trans = trans[:-2]
                trans += "yu"
            #Grammer Rule 4: This is when a small ょ appears
            if self._hirigana2[self._hirigana1.index(i.encode("utf-8"))] == "3":
                trans = trans[:-2]
                trans += "yo"
        return trans

    #This is the method to translate from Romanji to Hirigana
    def romanjiTranslate(self,input):
        s = list(input)
        trans = ""
        j = 0
        #Here even more character values had to be accounted for while transalting in the other direction. This might have been the hardest bit of the project.
        while True:
            #Check for Space
            if s[j] == " ":
                trans += " "
                j += 1
            #Case 1: Single character character.
            elif s[j] == "a" or s[j] == "o" or s[j] == "i" or s[j] == "e" or s[j] == "u" or s[j] == "n":
                trans += self._hirigana1[self._hirigana2.index(s[j])].decode("utf-8")
                j += 1
            #Case 2: If it includes a "ya".
            elif s[j+1] == "y" and s[j+2] == "a":
                trans += self._hirigana1[self._hirigana2.index((str(s[j])+"i"))].decode("utf-8") + self._hirigana1[self._hirigana2.index("1")].decode("utf-8")
                j += 3

            elif s[j+1] == "y" and s[j+2] == "u":
                trans += self._hirigana1[self._hirigana2.index((str(s[j])+"i"))].decode("utf-8") + self._hirigana1[self._hirigana2.index("2")].decode("utf-8")
                j += 3

            elif s[j+1] == "y" and s[j+2] == "o":
                trans += self._hirigana1[self._hirigana2.index((str(s[j])+"i"))].decode("utf-8") + self._hirigana1[self._hirigana2.index("3")].decode("utf-8")
                j += 3

            #Case 3: If there is a  っ
            elif s[j+1] == s[j]:
                trans += self._hirigana1[self._hirigana2.index("0")].decode("utf-8") + self._hirigana1[self._hirigana2.index(str(s[j+1])+str(s[j+2]))].decode("utf-8")
                j += 3

            #Case 4: If it is sha, sho, shu & cha, chu, cho
            elif s[j+1] == "h" and s[j+2] == "a":
                trans += self._hirigana1[self._hirigana2.index(("sha"))].decode("utf-8") + self._hirigana1[self._hirigana2.index("ha")].decode("utf-8")
                j += 3

            elif s[j+1] == "h" and s[j+2] == "o":
                trans += self._hirigana1[self._hirigana2.index(("sha"))].decode("utf-8") + self._hirigana1[self._hirigana2.index("ho")].decode("utf-8")
                j += 3

            elif s[j+1] == "h" and s[j+2] == "u":
                trans += self._hirigana1[self._hirigana2.index(("sha"))].decode("utf-8") + self._hirigana1[self._hirigana2.index("hu")].decode("utf-8")
                j += 3

            #Case 5: If its shi or chi
            elif s[j] == "s" and s[j+1] == "h" and s[j+2] == "i":
                trans += self._hirigana1[self._hirigana2.index(("shi"))].decode("utf-8")
                j += 3

            elif s[j] == "c" and s[j+1] == "h" and s[j+2] == "i":
                trans += self._hirigana1[self._hirigana2.index(("sha"))].decode("utf-8") + self._hirigana1[self._hirigana2.index("hu")].decode("utf-8")
                j += 3

            #Case 5: If it is ja, ju ,jo
            ################################

            #Case 6: All other characters
            else:
                try:
                    trans += self._hirigana1[self._hirigana2.index(str(s[j])+str(s[j+1]))].decode("utf-8")
                    j += 2
                except:
                    print("Invalid Character Present")

            if j == len(s):
                break

        return trans

    # Getters Implementation
    def get_sentencehiri(self):
        return self.__sentencehiri

    def get_sentenceromanji(self):
        return self.__sentenceromanji



class stats(study):
    def __init__(self):
        #Initialization of stats fields and Secret Function Fields : ))
        self.JasonMessage = "あなたのすきなアニメはなんですか"
        self.CathalMessage = "はじめまして"
        self.__hiristats = ""
        self.__katastats = ""
        self.__kanjistats = ""
        super().__init__()
    
    def __str__(self):
        return self.hirigana() + "\n" + self.katakana() + "\n" + self.kanji()

    def JasonsFunction(self):
        #If you find this function. It was created for our original Lecturer who loved anime. Its a bonus translation function.
        #All you have to do is call the correct method in this method to decode the secret message called "JasonMessage"
        self.JasonMessage = "あなたのすきなアニメはなんですか"
        return "\n"

    def CathalMessage(self):
        #As a welcome our class. Get it CLASS! Hahaha. Anyway, I left a message for you too. Hope you can translate.
        self.CathalMessage = "はじめまして"
        return "\n"

    #Returns the Stats of Hirigana Characters
    def hirigana(self):
        return f"There are {len(self._hirigana1)} characters in Hirigana. Hirigana are the base sounds used for all native Japanese words.\n"

    #Returns the Stats of the katakana Characters
    def katakana(self):
        return f"There are {len(self._katakana1)} characters in Katakana. Katakana are the symbols for the base sounds of foriegn words in the Japanese language\n" 

    #Returns the stats of the Kanji Characters
    def kanji(self):
        return f"There are 1000's of Kanji that exist. You are studying {len(self._kanji1)} Kanji. Kanji are all the symbols that represent words, ideas and concepts.\n"



def play():
    #Tried to use match and case here. But python isnt updated enough so I used if statements
    #Initilzing all classes
    T = translate()
    D = daily()
    S = study()
    St = stats()
    #This part is the game implementation
    print("Welcome to your Japanese Converter/Studier")
    print("In this app you can: \n 1.Translate Romanji/Hirigana \n 2.Do whole Hirigana tests \n 3.Do daily Hirigana tests and more.\n\n")
    time.sleep(5)
    while True:
        #Initial Choices. Give it a play!
        print("You can choose to \n1.Translate Japanese \n2.Study Japanese \n3.Daily Japanese Review \n4.Extra Options")
        k = input("Enter: (1/2/3/4)\n")

        #Translate Romanji/Hirigana
        if k == "1":
            print("Would you like to 1.Translate Hirigana 2.Translate Romanji 3.Do Sample Translations")
            k = input("Enter: 1/2/3\n")
            if k == "1":
                p = input("Enter your hirigana to be converted: \n")
                print(T.hiriganaTranslate(p))
            
            if k == "2":
                p = input("Enter your romanji to be converted: \n")
                print(T.romanjiTranslate(p))

            if k == "3":
                T.exampleTranslate()
            else:
                print("Invalid Input: Please try again")

        #Study Japanese
        elif k == "2":
            print("Would you like to 1.Do hirigana review 2.Do katakana review 3. Do Kanji review 4.Do hirigana sentence review. 5.Do a katakana sentence review \n")
            k = input("Enter: 1/2/3/4/5")
            if k == "1":
                S.hirigana()
            elif k == "2":
                S.katakana()
            elif k == "3":
                S.kanji()
            elif k == "4":
                S.hiriSentenceTest()
            elif k == "5":
                S.kataSentenceTest()
            else:
                print("Invalid Input: Please try again")
    
        #Daily Hirigana Practice
        elif k == "3":
            print("Would you like to 1. Daily Hirigana Practice 2. Daily Katakana practice \n")
            k = input("Enter: 1/2")
            if k == "1":
                print("Your daily Hirigana Practice: \n")
                D.dailyhirigana()
            elif k == "2":
                print("Your daily Katakana Practice: \n")
                D.dailykatakana()
            else:
                print("Invalid Input: Please try again")

        #Other Options. Some Secret Options 
        elif k == "4":
            print("These are your options:")
            print("1.JasonsFunction(:) ) 2.Cathals Function(:D) 3.Hirigana Stats 4.Katakana Stats 5. Kanji Stats 6. All Stats 7.Get the sample Sentences")
            k = input("Enter: 1/2/3/4/5/6/7")
            print(k)
            if k == "1":
                print("Oh, it looks like there isnt much in the function. Maybe try scrolling up to edit it. You might find a secret!")
                St.JasonsFunction()

            elif k == "2":
                print("Looks like there isnt much in this function. Maybe scroll up to find a secret in this fucntion! :D")
                St.CathalMessage()
            elif k == "3":
                print(St.hirigana())
            elif k == "4":
                print(St.katakana())
            elif k == "5":
                print(St.kanji())
            elif k == "6":
                print(St.__str__())
            elif k == "7":
                #Sample hirigana Sentences being Retrieved
                print("The sample Hirigana Sentences")
                T.get_sentencehiri()

                print("The sample Romanji Sentences")
                T.get_sentenceromanji()
            else:
                print("Invalid Input: Please try again")
        else:
            print("Invalid Input: Please try again")
play()
