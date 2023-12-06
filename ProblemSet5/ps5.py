# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Bekhruz Abdullakhujaev
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
            pubdate = pubdate.astimezone(pytz.timezone('EST'))
            pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
    
    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate.replace(tzinfo=None)

        


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError


# PHRASE TRIGGERS

# Helper func: validate_phrase(phrase)
def validate_word(phrase):
    phrase_copy = ""
    for l in phrase:
        if l not in string.punctuation:
            phrase_copy = phrase_copy + l
        else: 
            phrase_copy = phrase_copy + " "
    return " ".join(phrase_copy.lower().split())

def exists_in_list(list1, list2):
    for i in list1:
        if i not in list2:
            return False
    return True

def convert_to_datetime(time):
    format = "%d %b %Y %H:%M:%S"
    return datetime.strptime(time, format).replace(tzinfo=None)
    

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase.lower()
    
    def get_phrase(self):
        return self.phrase
   
    def is_phrase_in(self, text):
        return self.phrase in text and exists_in_list(self.phrase.split(), text.split())

# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
  
    def evaluate(self, story):
        title = story.get_title()
        return self.is_phrase_in(validate_word(title))
    
    
# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)
    
    def evaluate(self, story):
        description = story.get_description()
        return self.is_phrase_in(validate_word(description))

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    #    Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
    #    Convert time from string to a datetime before saving it as an attribute.
    def __init__(self, datetime_string):
        self.datetime = convert_to_datetime(datetime_string)
    
    def get_time(self):
        return self.datetime
    
    

# Problem 6
class BeforeTrigger(TimeTrigger):
    def __init__(self, datetime_string):
        TimeTrigger.__init__(self, datetime_string)
    
    def evaluate(self, story):
        return self.datetime > story.get_pubdate()

class AfterTrigger(TimeTrigger):
    def __init__(self, datetime_string):
        TimeTrigger.__init__(self, datetime_string)
    
    def evaluate(self, story):
        return self.datetime < story.get_pubdate()
    
    
# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, trigger):
        Trigger.__init__(self)
        self.trigger = trigger
    def get_trigger(self):
        return self.trigger
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, trigger_1, trigger_2):
        Trigger.__init__(self)
        self.trigger_1 = trigger_1
        self.trigger_2 = trigger_2
    def get_trigger_1(self):
        return self.trigger_1
    def get_trigger_2(self):
        return self.trigger_2
    def evaluate(self, story):
        return self.trigger_1.evaluate(story) and self.trigger_2.evaluate(story)
        

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, trigger_1: Trigger, trigger_2:Trigger) -> None:
        super().__init__()
        self.trigger_1 = trigger_1
        self.trigger_2 = trigger_2
    def get_trigger_1(self):
        return self.trigger_1
    def get_trigger_2(self):
        return self.trigger_2
    def evaluate(self, story):
        return self.trigger_1.evaluate(story) or self.trigger_2.evaluate(story)
        


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    result = []
    for s in stories:
        for t in triggerlist:
            if t.evaluate(s):
                result.append(s)
    return result



#======================
# User-Specified Triggers
#======================
# Problem 11 
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # DISCLAIMER: I got THE 257 - 287 LINES OF CODE from https://github.com/Per48edjes/MIT-6-0001-PS5/blob/master/ps5.py
    # Initialize trigger mapping dictionary
    t_map = {"TITLE": TitleTrigger,
            "DESCRIPTION": DescriptionTrigger,
            "AFTER": AfterTrigger,
            "BEFORE": BeforeTrigger,
            "NOT": NotTrigger,
            "AND": AndTrigger,
            "OR": OrTrigger
            }

    # Initialize trigger dictionary, trigger list
    trigger_dict = {}
    trigger_list = [] 

    # Helper function to parse each line, create instances of Trigger objects,
    # and execute 'ADD'
    def line_reader(line):
        data = line.split(',')
        if data[0] != "ADD":
            if data[1] == "OR" or data[1] == "AND":
                trigger_dict[data[0]] = t_map[data[1]](trigger_dict[data[2]],
                        trigger_dict[data[3]])
            else:
                trigger_dict[data[0]] = t_map[data[1]](data[2])
        else: 
            trigger_list[:] += [trigger_dict[t] for t in data[1:]]

    for line in lines:
        line_reader(line)
    return trigger_list 

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        
        triggerlist = read_trigger_config("ProblemSet5\\triggers.txt")
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "New York Times Top News"
        title = StringVar()
        title.set(t)    
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from New York Times Top Stories RSS news feed
            stories = process("https://rss.nytimes.com/services/xml/rss/nyt/World.xml")

            # Get stories from Yahoo's Top Stories RSS news feed
            #stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)
            print("stories ", stories)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

