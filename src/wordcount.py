from string import punctuation, digits
import fileinput
import sys
import median

class WordCount:

    def __init__(self):
        """Initialize class variables"""
        self.total_count = {}
        self.line_count = {}
        self.files = sorted(sys.argv[1:])
        self.file_input = fileinput.FileInput(self.files)
        self.exclude = set(punctuation+digits)
        self.median = median.Median()

    def addWord(self, count, x):
        """adds word to dictionary and keeps count of
        unique instances."""
        if x in count:
            count[x] += 1
        else: count[x] =1

    def write_output(self, out_file='', text=''):
        f=open(out_file, 'a')
        f.write(str(text))

    def crunchWords(self, calc_median=True, word_out_file='', median_out_file=''):
        """ Here we add words to
        1. the dictionary that indexes all words and,
        2. the dictionary that indexes a single line.
        from 2., we calculate the the running median."""

        for line in self.file_input:
            words=line.split()
            for word in words:
                # do simple data cleaning.

                word = ''.join(punc for punc in word if punc not in self.exclude)

                self.addWord(self.line_count, word)
                self.addWord(self.total_count, word)

            if calc_median == True and len(self.line_count) > 2:
                #we will ignore blank lines and those with only a single word
                #and write to the output median file for each line

                self.median.add(len(self.line_count))
                median = self.median.get()
                self.write_output(median_out_file , str(median)+'\n')

            #clear the running median dictionary input
            self.line_count = {}

        for key in self.total_count:
            #format the total-unique-word output file

            formatted_text=key.ljust(20)+'\t\t\t'+str(self.total_count[key]).ljust(30)+'\n'
            self.write_output(word_out_file, formatted_text)