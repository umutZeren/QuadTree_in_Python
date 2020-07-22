# QuadTree_in_Python
this python script implements a quadtree for image creation dependent on single charecter input representation for image sectors.  
plus sign divides images to four equal section named as q1 q2  
                                                     q4 q3  
program takes input from standart input.  


input format :  + (plus sign ) divides image representation to four equal parts. it takes input charecters of the divided sector in clocwise rotation.  
              python quad_Tree.py < input  
              ex: q1 q2     
                  q4 q3  
                input one +....  
                output one : ..  
                             ..  
               input 2: +.**.  
               output2 :  
                         .*  
                         .*  
               input 3: +o+xoox+ooxox  
               python quad_Tree.py < input  
               output 3:  
                        ooxo  
                        ooxo  
                        xxoo  
                        xxox  
               input 4: +.+..+**..+.*.*++..*.+*..*+*..*+.*..+.+.**.+*..*.  
               output4:  
                       ........  
                       ........  
                       .....***  
                       ....*...  
                       ...*..*.    
                       ...*.**.    
                       ..*..**.    
                       ..*...*.    
