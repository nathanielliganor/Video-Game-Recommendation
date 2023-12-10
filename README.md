# Video Game Recommendation #

This is a Python program that manages a user's video game collection.

Important notes: install requests, pickle, and random packages

## How to Use ##
Start the game collection program

Answer whether you want to load a previously saved collection. If yes, then provide the filename of the saved collection.

Once the collection is loaded, enter the attribtue for the games you are searching for from your collection.

Review the listed games that match your search request.

Reiterate these steps for additional searching.

If your collection is updated and you want it saved, provide a new name for this updated collection when prompted.


## Features and Functions ##

**File Loading:** When the program first launches, the user will be asked if they want to load an existing video game collection they have previously created using this program. Users are then required to enter the name of that particular file.

**Game Search:** On successful loading of the collection file, users will be prompted to input a video game attribute of their choice, which can include attributes such as a specific platform, genre, or other tags linked with the video game. The program will then deliver a list of games from the user's collection that corresponds to their search request.

**Further Searching:** After the first search, the program will ask the user if they want to conduct another search. If the users answer "yes", the program will then ask the users if they would like to add a new game to their collection. This gives the users the option of either entering a new video game title to their collection or say no. Once the user enters a new game title or decides not to, the program will repeat the process of asking for an attribute and providing the corresponding video game titles in their collection that is updated with their new video game entry.

**Collection Saving:** If the users choose "no" to further searching, the program then asks if they want to save their current collection if there has been a new game added. If the user chooses to save, they will be prompted to name their new collection.




