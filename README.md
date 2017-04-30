# MCTEXTGEN
### MM Project 1 - FRI UNI 2017

## Octave scripts
Examples of function calls can be found inside scripts and `script_examples.m` file.
To apply punctuation rules, run `run.sh` script which will use dot, exclamation and question mark as separate words, further
improving quality of generated text. In Python script, this is implemented by default.

* mctextgen.m - generates text files from Markov Chain transition matrix and word vector
* matrixgen.m - generates Markov Chain transition matrix and word vector
* questiongen.m - generates single line answer/question pair

## Python scripts

Install required libraries by running `sudo pip3 install -r requirements.txt`.

Script can be run with `python3 main.py <action> {args}`

Actions select the mode of script:
* `interactive` - enter a shell with basic commands
* `gen` - calculate data and generate some text
* `build`- calculate data and save it to file for reuse
* `read` - read Pickle dump and generate some text

**Action: GEN**  
Reads source text file, build transition matrix and generates a requested length of text.
Required arguments:
* `-if` - path text source file (ex: butalci.txt)
* `-of` - filename, where to output generated text
* `-l` - length of requested text


**Action: READ**  
Reads a Pickle dump to RAM and generates requested length of text, which is written to file.
Required arguments:
* `-rf` - path of Pickle dump to read (must contain transition matrix)
* `-of` - filename, where to output generated text
* `-l` - length of requested text


**Action: BUILD**  
Reads a source text, builds a transition matrix and dumps it to output binary file.
Required arguments:
* `-if` - path text source file (ex: butalci.txt)
* `-df` - filename of Pickle dump

**ACTION: INTERACTIVE**  
Enters a shell where various commands can be used interactively to avoid costly and slow data reloads.
 Commands:  
 * `read <filename>` - read text file to memory
 * `load raw` or `load dump <file>` - raw: builds transition matrix from text currently in memory. Dump: reads transition matrix from binary Pickle dump file.
 * `dump <filename>` - Save current transition matrix to Pickle dump for presistence between sessions
 * `gen <len> <out>` - Generate a text of length `len`. `out` parameter describes where to write, if `-`, then data gets written to stdout, otherwise to file.
 * `save <filename>` - Save last generated text to `filename`.
 * `!!` or `!! <command>`  -  first reruns previous command, second one reruns previous command with `command` argument appended.
 * `cd <path>` - change directories
 * `ls` - list files in current directory
 * `pwd` - show absolute path of current directory
 * `exit` - exit script
 * `rm <filename>` - delete a file
 * `clean` - remove all session data
 * `show` - display what data is currently loaded and some statistics
 
 
 Typical session:
 ```
 > read ../../data/butalci.txt  #loads text to RAM
 > load raw                     #calculates matrix
 > gen 10 -                     #generate a text 10 words long, to stdout
 > dump butalci.dump            #save data
 > clean                        #delete current data
 > load dump butalci.dump       #reload data from disk
 > show                         #display stats
 > gen 100 -                    #generate 100 words
 > !!                           #rerun generation
 > save iLikeThis.txt           #save previously generated text to file
 ```
 