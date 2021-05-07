This project aims to process the meeting transcript files and generate 
required output.

It takes meeting transcript file as input and does,

1. Preprocesses the meeting transcript file
2. Generates action statements,
3. Generates summary of meeting.

The files can be installed in any directory and internet connection is
required to access tensor flow hub. Later this dependency will be
removed.

All the data set files will be stored in NewDataset folder.
The file process_seplines.py contains the functions to preprocess
the transcript file.
The file process_transcript contains the functions to generate
the action statements and summary of meeting transcript.

The process_transcripts.py has the below syntax.
usage: process_transcripts.py [-h] -f TRANSCRIPT_FILENAME -o OUTPUT_DIR
                              [-a ACTIONS] [-m SUMMARY] [-n OTHERS]

-f is used to give the input meeting transcript file.
-o is used to give the output directory path where the actions.txt,
	nonactions.txt and summary.txt files will be stored
-a is used to generate only action statements
-m is used to generate only summary statements
-n is used to generate only non-action statements

An example of the usage of the script is given below.

python process_transcripts.py -f ../txtfiles/transcript_filename.txt -o ./outputs/Action/


