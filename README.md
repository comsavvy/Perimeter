# Perimeter
This project is about:
* Reading from a files containing points
* Calculating the perimeter of one point to the other
* Finding the maximum and minimum perimeter
* Average length of all the perimeter
* Sum of all the perimeter
* Passing the files from the ```command prompt```
* Saving the return values of the ```summarize points``` to a text file called ```total_output.txt```
* Making sure the ```Point class``` can accept any length of point.

The two available module that can process points are
* <a href='https://github.com/comsavvy/Perimeter/blob/master/perimeter.py'>perimeter.py</a>
* <a href='https://github.com/comsavvy/Perimeter/blob/master/perimeter.sh'>perimeter.sh</a> ```Bash script``` which depend on ```perimeter.py```

Both of this two file can accept any files containing point, but the main difference is that;
* <p><a href='https://github.com/comsavvy/Perimeter/blob/master/perimeter.py'>perimeter.py</a> will only return the summary to the terminal</p>
while
* <a href='https://github.com/comsavvy/Perimeter/blob/master/perimeter.py'>perimeter.sh</a> will save the output into <a href='https://github.com/comsavvy/Perimeter/blob/master/total_output.txt'>```total_output.txt```</a> and also display the content to the terminal.<br />
The pattern that was used to generate the current <a href='https://github.com/comsavvy/Perimeter/blob/master/total_output.txt'>```total_output.txt```</a> is<br /> 
### ./perimeter example* datatest* testing_many_dimension.txt
