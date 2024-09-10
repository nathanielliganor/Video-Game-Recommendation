import pickle
from BinarySearchTree import BinarySearchTreeNode

def main():
    tree = None

    # Load an existing video game collection from a file
    # If the user chooses to load an existing collection,
    # the program will prompt the user for the name of the
    # file containing the collection.
    print("Welcome to the Video Game Finder!")
    load = input("Would you like to load an existing video game collection from a file? (yes/no): ")
    if load.lower() == "yes":
        filename = input("What is the name of the file?: ")
        with open(filename, "rb") as treeFile:
            try:
                tree = pickle.load(treeFile)
                print("Video game collection loaded successfully!")
            except Exception as e:
                print("Error loading video game collection.")
                return
        BinarySearchTreeNode.query_tree(tree)
        keep_searching = input("Would you like to search again? (yes/no): ")
    else:
        keep_searching = "yes"
        search_term = input('Add a new game to your collection: ')
        tree = BinarySearchTreeNode.fetch_data(search_term, tree)

    # Add a new game to the collection
    # The user can add a new game to the collection by entering
    # the title of the game.
    while keep_searching.lower() == "yes":
        search_term = input('Add a new game to your collection? (Enter new game title or no): ')
        tree = BinarySearchTreeNode.fetch_data(search_term, tree)
        BinarySearchTreeNode.query_tree(tree)
        keep_searching = input("Would you like to search again? (yes/no): ")

    # Save the collection for later
    save = input("Would you like to save this collection for later? (yes/no): ")

    # If the user chooses to save the collection, the program will
    # prompt the user for the name of the file to save the collection to.
    if tree and save.lower() == "yes":
        filename = input("Please enter a file name: ")
        with open(filename, "wb") as treeFile:
            pickle.dump(tree, treeFile)
        print("Thank you! The collection has been saved.")

    # Exit the program
    print("Bye!")

if __name__ == '__main__':
    main()
