""" 
   !--------------------------------------------------------------------------!
   ! LICENSE INFO:                                                            !
   !--------------------------------------------------------------------------!
   !    This file is part of localCIDER.                                      !
   !                                                                          !
   !    Version 0.1.0                                                         !
   !                                                                          !
   !    Copyright (C) 2014, The LocalCIDER development team (current and      !
   !                        former contributors): Alex Holehouse, James       !
   !                        Ahad, Rahul K. Das.                               !
   !                                                                          !
   !    localCIDER was developed in the lab of Rohit Pappu at Washington      !
   !    University in St. Louis. Please see the website for citation          !
   !    information:                                                          !
   !                                                                          !
   !    http://pappulab.github.io/LocalCIDER/                                 !
   !                                                                          !
   !    For more information please see the Pappu lab website:                !
   !                                                                          !
   !    http://pappulab.wustl.edu/                                            !
   !                                                                          !
   !    LocalCIDER is free software: you can redistribute it and/or modify    !
   !    it under the terms of the GNU General Public License as published by  !
   !    the Free Software Foundation, either version 3 of the License, or     !
   !    (at your option) any later version.                                   !
   !                                                                          !
   !    LocalCIDER is distributed in the hope that it will be useful,         !
   !    but WITHOUT ANY WARRANTY; without even the implied warranty of        !
   !    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         !
   !    GNU General Public License for more details.                          !
   !                                                                          !
   !    You should have received a copy of the GNU General Public License     !
   !    along with LocalCIDER.  If not, see <http://www.gnu.org/licenses/>.   !
   !--------------------------------------------------------------------------!
   ! AUTHORSHIP INFO:                                                         !
   !--------------------------------------------------------------------------!
   !                                                                          !
   ! MAIN AUTHOR:   Alex Holehouse                                            !
   !                                                                          !
   !--------------------------------------------------------------------------!

   
   File Description:
   ================
   
   This is one of the key user interface/API files from which users (AKA you!)
   should use to access localCIDER.

   For a full description please see the documentation



"""

from backendtools import warning_message, status_message

from data.aminoacids import ONE_TO_THREE

class SequenceFileParserException(Exception):
    pass


class SequenceFileParser:
    """
        SequenceFileParser is a stateless sequence parsing machine. 
        You feed it a filename and it returns a sequence as string. Allows for the expansion of the type of sequence which can
        be dealt with.

    """

    def __init__(self):
        """ No parameters required """
        pass
    

    def parseSeqFile(self, filename,silent=False):
        """
        The parseSeqFile function is the meat of the SequenceFileParser object, and carrys out stateless parsing of a sequence file to a single, 
        unbroken string which contains only valid amino acids. 


        INPUT:
        Filename  | Name of a file to parse (string)
        Silent    | Defines if the parsing operation should be Silent, or if 
                    there should be messages prinited to screen
        
        OUTPUT:
        Amino acid sequence in a string

        """
        # read file to end
        with open(filename) as filehandle:
            content = filehandle.readlines()

        header=False
        seq=""

        # cycle over each line in the file
        for line in content:
            line=line.strip()

            # empty line
            if len(line) == 0:
                continue
            
            # if you have a header line 
            if line[0] == ">":

                # if the header flag had already been flicked then raise an exception (indicative of  multiple sequences in a single file)
                if header == True:
                    raise KeyFileException("\n\nERROR: During parsing of sequence file found a second header section. Sequence files must be a single file")

                # if it has not, flick the header flag to on
                header=True
                continue
            elif len(line) > 0:
                # validate sequence (raises exception if something is bad) and append to the growing sequence string
                line=self.__validSeq(line)
                seq=seq+line

        if not silent:
            status_message("Parsed sequence [" + str(len(seq)) + " residues]:\n"+seq)
        return seq


    def __validSeq(self, sequence):
        """ 
        Internal function which validates if a [region of] 
        a sequence is a valid protein sequence.

        The validation skips spaces and numbers, but will raise an exception on any other character
        
        Super dumb but good first line of validation
        """

        parsed_seq =""

        # for each residue in the sequence
        for i in sequence:
            
            # if the residue is not in the three letter code
            if i not in ONE_TO_THREE.keys():
                if i == " ":
                    # skip spaces
                    continue
                elif i in "1234567890":
                    warning_message("Found '" + i + "' in sequence, stripping out and ignoring...")
                    # strip out numbers (useful for copy/pasted FASTA formats)
                    continue 
                else:
                    raise SequenceFileParserException("\n\nERROR: Invalid sequence file, found [" + i + "] in sequence region\n\n"+sequence+"\n\n")
            # if the residue *is* one of the 20 AAs then append to the growing sequence
            else:
                parsed_seq=parsed_seq+i
        return parsed_seq