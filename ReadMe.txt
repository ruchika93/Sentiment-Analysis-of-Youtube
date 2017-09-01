Refer tp CSC555_Term Paper for a complete understanding of the project.

How to execute the project.

Prerequisites:
- The user should have a Google Developer account.
- Obtain client_secrets.json and youtube_v3_discoverydocument.json from the YouTube Developer project profile and place them in the root folder where all the python files are   present.
- Python 2.7 or higher should be installed on the system.
- Youtube API package should be installed.
- NLTK package should be installed.
- TextBlob package should be installed.
- Pandas package should be installed.
- Create folders: "video_ids", "fetched_comments" and "output_csv" in the root folder.

Execution Steps:
- In the command prompt, navigate to the source folder and locate "youtube_search.py".
- Open the file and put your Google Developer's ke in the spaceprovided at line 22.
- Enter the search phrase in line 64.
- Save the file and execute the file using the terminal with "python youtube_search.py".
- This would create a txt file in video_ids folder.

- Open "getComments.py" and put the name of file created in the previous step at line 109
- Save the file and execute.
- This would create multiple json files in the folder fetchedComments.

- Open "senti_analysis.py" and at line 14 and line 23 put the path of the folder where the json files were created in the last step.
- Give the path and name of the output csv file at line 19.
- Give the desired filter words in line 37 for filtering out the comments which do not contain these words.
- Save and execute the file.
- This would create a csv file in the output_csv folder.

- Open "median_calc.py" and enter the filename created in the last step at line 3 and the target file name at line 5.
- Save and execute the file.
- This would give you a csv file which will have the median polarity for each date.
- Plotting a graph on these two columns will give you the graph.
