##################################################################################
#
#  Product - Transcript Summary
#  File Name - process_seplines.py
#
#  Authors - Chandrashekar B N , Srinivas Chakravarthy
#
##################################################################################
#
#  This file does the preprocessing of the meeting transcript data 
#
#
###################################################################################

import pandas as pd
import os, sys, glob

def gen_sep_lines(filename):
    fname = open(filename, 'r')
    flines = fname.readlines()
    count = 0
    prev_line = ""
    speaker_name = ""
    prev_speaker_name = ""
    final_lines = []
    sent_count = 0
    prev_sent_count = 0
    valid_line = True
    #end_of_transcript = False
    for line in flines:
        #if end_of_transcript == True:
            #break

        if line.find("____________________") != -1:
            count = count + 1

            if count == 1:
                #print ("Found start of line")
                continue
            else:
                #end_of_transcript = True
                #print ("Found end of line")
                break
        
        if count == 0:
            continue

        # Skip the noisy sentences
        if line.find("joined the conference") != -1:
            continue
        if line.find("left the conference") != -1:
            continue

        # Skip the time stamp
        elecount = 0
        for ele in line:
            elecount = elecount + 1
            if ele == '<':
                continue
            if ele == '>':
                # Skip the space after >
                elecount = elecount + 1
                line = line[elecount:]
                break
       
        # Parse the rest of the line which has speaker name at the start of line
        elecount = 0
        for ele in line:
            elecount = elecount + 1
            # Get the name of the speaker
            flag_onlyspace = False
            if ele == ':':
                valid_line = True
                speaker_name = line[:(elecount-1)]
                #speaker_name = speaker_name.strip()

                # Skip the space after :
                line = line[elecount+1:]

                if speaker_name.isspace() == True:
                    flag_onlyspace = True
                    break
                line = speaker_name+" said "+line
                break

        if valid_line == True:
            valid_line = False
            line = line.split('\n')[0]
            line = line.strip()
            if line[-1] != '.':
                line = line+'.'
            final_lines.append(line)
        else:
            # The transcript has muliple lines with new line by the same speaker
            if len(line) != 0:
                last_line = final_lines.pop(len(final_lines) - 1)
                line = line.strip()
                line = last_line[:-1] + ' '+ line+'.' 
                #print ("last line: {} line: {}".format(last_line, line))
                final_lines.append(line)
        
    #print (final_lines)

    df = pd.DataFrame(final_lines)
    df.to_csv('results_seplines.txt', header=None, index=None, sep='\n', mode='w')

    return "results_seplines.txt"
