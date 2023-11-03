## Python Test assignment-Developer (Junior)   

Write a news parser from the website ByBit:   
https://announcements.bybit.com/en-US/?category=&page=1   

#### The parser should:   
1. Execute JS.   
2. Request fresh data 1 time per second (bypass possible CDN blocking and caching).   

If there is a new news item, then save the exact time of its appearance, the title and the link to it in the format.csv

The new data is saved in the file ```new_data.csv```. Located at ```parser-by-bit/tests/fixtures/new_data.csv```.

#### Minimum requirements:   
1. Python.
2. Pip.
3. Poetry.

#### Install:
1. Download the project.
2. Go to the root directory of the project.
3. Log in to the virtual environment poetry by the command ```poetry shell```
4. Install the required packages with the command ```make install```
5. Run the file '''main.py'''.  Located at '''parser-by-bit/parse/main.py'''.
