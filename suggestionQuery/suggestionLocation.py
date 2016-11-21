#give a criteria
#return the best location

import numpy as np
import glob
import os

def suggestion(string):
    
        input_para_data = string.strip().split(',');
        
        location_list = ["CITY CENTER","CLOVERDALE","FLEETWOOD","GUILDFORD","NEWTON","SOUTH_SURREY"];

        score_list=[0,0,0,0,0,0]
    
        #files
        population_file = open("/Users/clarence/Desktop/GitHub/TelusDatathon/tableau/population_new.csv",'r');
        language_file = open("/Users/clarence/Desktop/GitHub/TelusDatathon/tableau/language_area.txt",'r');
        if "school" in input_para_data:
            score_list[0]+=1;
            score_list[2]+=1;
            score_list[4]+=1;
        
        if "Cantonese" in input_para_data:
            for line in enumerate(language_file):
                line = str(line[1]);
                if line.startswith('#'):
                    continue;
                    #Language	CITY_CENTRE	CLOVERDALE	FLEETWOOD	GUILFORD	NEWTON	SOUTH_SURREY
                tobesplit = line;
                data= tobesplit.strip().split('\t');
                if "Cantonese" not in data:
                    continue;
                for index in range(1,6):
                    if data[index] !="0":
                        score_list[index]+=1;

        print location_list[score_list.index(max(score_list))];

if __name__ == '__main__':
    suggestion("Cantonese,school")



