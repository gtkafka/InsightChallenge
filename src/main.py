__author__ = 'kafka'

import wordcount
import os

def main():

    #define working input and output directories and files.

    dir = os.path.dirname(os.path.abspath(__file__))
    pdir = os.path.abspath(os.path.join(dir, os.pardir))

    output_dir   = pdir+'/tweet_output'
    w_out= output_dir+'/ft1.txt'
    m_out= output_dir+'/ft2.txt'
    files = [w_out, m_out]

    #make paths and delete existing files.

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for file in files:
        if os.path.isfile(file):
            os.remove(file)

    #run the script
    #have the ability to toggle on/off calculating running median
    word_count = wordcount.WordCount()
    word_count.crunchWords(calc_median     = True,
                           word_out_file   = w_out,
                           median_out_file = m_out,
                           )

if __name__ == '__main__':
    main()
