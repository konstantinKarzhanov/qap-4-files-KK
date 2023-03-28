<h1>QAP-4. Python Projects</h1>

<h2>#qap-4_project-1_lists-and-datafiles.py: Car Insurance Calculator</h2>

<p>This is a Python script that calculates car insurance premiums based on customer information, insurance options selected, and the data that stored in defaults file "OSICDef.dat".</p>

<h3>NOTE</h3>
<p>The script can read the data from files using readDefaultsFile() function.
The function is designed to read data from a file and return it in a structured form of a list or tuple. It can handle files that are structured with or without a separator. In this specific program, I used the file "OSICDef.dat" which contains the data separated with "=" (key = value format).</p>

<p>If we decide to read the data from the file containing Only values we need to remove the specified separator "=" on line 212 (LIST_CONSTANTS = readDefaultsFile(FILE_DEFAULTS, "=")) and change the name of the file on line 210 (FILE_DEFAULTS = "newFileName")</p>

<h3>REQUIREMENTS</h3>
<p>This script was written using Python 3.9.6. It requires the following Python modules:</p>
<ul>
<li>datetime</li>
<li>atexit</li>
<li>re</li>
</ul>
<h3>USAGE</h3>
<p>To use this script, simply run it from the command line using Python:</p>
<ul>
  <li>python3 qap-4_project-1_lists-and-datafiles.py</li>
</ul>

<p>Follow the prompts to enter the customer information and insurance options. The script will then display a summary of the insurance premium and total cost.</p>

<h3>INPUTS</h3>
<p>The script prompts the user for the following information:</p>
<ul>
<li>Customer first name</li>
<li>Customer last name</li>
<li>Customer street address</li>
<li>Customer city</li>
<li>Customer province</li>
<li>Customer postal code</li>
<li>Customer phone number</li>
<li>Number of cars to insure</li>
<li>Whether the customer wants extra liability coverage</li>
<li>Whether the customer wants glass coverage</li>
<li>Whether the customer wants loaner car coverage</li>
<li>Whether the customer wants to pay in monthly installments or in one payment</li>
</ul>
<h3>OUTPUTS</h3>
<p>The script displays the following information:</p>
<ul>
<li>Customer name, full address and phone number</li>
<li>Number of cars insured</li>
<li>Extra liability coverage (selected option Yes/No)</li>
<li>Glass coverage (selected option Yes/No)</li>
<li>Loaner car coverage (selected option Yes/No)</li>
<li>Insurance premium</li>
<li>Extra liability coverage (if selected)</li>
<li>Glass coverage (if selected)</li>
<li>Loaner car coverage (if selected)</li>
<li>Total insurance premium</li>
<li>HST</li>
<li>Total cost</li>
<li>Invoice date</li>
<li>Monthly payment (if "M" was selected)</li>
<li>Next Payment day (if "M" was selected)</li>
</ul>
  
 
<h2>#qap-4_project-1_matplotlib_year-sales-graph.py: Sales Tracker</h2>

<p>This is a program designed to help you track your sales data for each month and display it on a graph.</p>

<h3>REQUIREMENTS</h3>
<p>This script was written using Python 3.9.6. It requires the following Python modules:</p>
<ul>
<li>matplotlib</li>
<li>calendar</li>
</ul>
  
<h3>USAGE</h3>
<p>To use this script, simply run it from the command line using Python:</p>
<ul>
<li>python3 qap-4_project-1_matplotlib_year-sales-graph.py</li>
</ul>

<h3>INPUTS</h3>
<p>Once the program is running, it will ask you to enter the sales amount for each month. Simply enter a number for each month, or type "STOP" to finish entering data and display the graph.</p>

<p>If you enter an invalid value or leave a field blank, the program will prompt you to try again or exit.</p>

<h3>OUTPUTS</h3>
<p>After entering all the data, the program will display a graph of your sales data for each month.</p>


<h2>License</h2>
<p>These projects is licensed under the terms of the MIT license.</p>

