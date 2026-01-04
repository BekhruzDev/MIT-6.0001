
def get_trigger_name(line_string):
    list = line_string.split(',')
    return list[1]
    
def main():
    print(get_trigger_name('t1,TITLE,election'))

if (__name__ == "__main__"):
    main()