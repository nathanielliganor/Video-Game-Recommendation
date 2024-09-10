import requests
import random

class BinarySearchTreeNode:

    def __init__(self, name):
        self.name = name
        self.children = []

    def insert(self, node):
        self.children.append(node)

    def search(self, name):
        queue = [self]
        while queue:
            current_node = queue.pop(0)
            if current_node.name == name:
                return current_node
            else:
                queue.extend(current_node.children)
        return None

    def recommend(self):
        games = [c.name for c in self.children]
        num_of_games = min(5, len(games))
        return random.sample(games, num_of_games)

    ## Test tree
    def display_tree(self, node, level=0):
        print("     " * level + node.name)
        for child_node in node.children:
            self.display_tree(child_node, level + 1)

    @staticmethod
    def query_tree(tree):
        '''
        Queries the binary search tree by a specified attribute and provides a list of recommended games.

        Parameters:
        tree (BinarySearchTreeNode): The root node of the tree containing the video game data.
        '''
        attribute = input("Enter video game attribute: ")
        node = tree.search(attribute)
        if node:
            games = node.recommend()
            print(f"Recommended {attribute} games in your collection: {games}")
        else:
            print(f"No {attribute} games found in your collection.")

    def fetch_data(search_term, tree=None):
        '''
        this function fetches video game data from the RAWG API and
        adds to the tree

        Parameters:
        search_term (str): The title of the video game to look up in the API.

        tree (BinarySearchTreeNode, optional): The root node of the existing tree. 
        If None, a new tree is created. Defaults to None.

        Returns:
        BinarySearchTreeNode: The root node of the tree after the video game data has been added.
        '''
        # if there is no tree create a new one
        if tree is None:
            tree = BinarySearchTreeNode('Video Games')

        api_key = "27f9898959fa47b59eadb89d4ff0b71b"
        url = f'https://api.rawg.io/api/games?key={api_key}&search={search_term}'
        game_data_list = []

        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                games = data.get('results', [])

                for game in games:
                    title = game.get('name', 'N/A')
                    platforms = game.get('platforms', []) or []
                    names_list = [platform_info['platform']['name'] for platform_info in platforms]
                    rating = game.get('rating', 'N/A')
                    esrb_rating = game.get('esrb_rating', {}).get('name', 'N/A')
                    tags = [tag.get('name', 'N/A') for tag in game.get('tags', []) if tag.get('language', 'N/A') == 'eng']
                    release_date = game.get('released', 'N/A')
                    screenshots = [screenshot.get('image', 'N/A') for screenshot in game.get('short_screenshots', []) or []]

                    game_data = {
                            'title': title,
                            'platforms': names_list,
                            'rating': rating,
                            'esrb_rating': esrb_rating,
                            'tags': tags,
                            'release_date': release_date,
                            'screenshots': screenshots
                        }

                    game_data_list.append(game_data)

            else:
                print()
        except:
            print("Error fetching data from the API.")

        # loop through the game data and insert them into the tree
        for game in game_data_list:
            game_node = BinarySearchTreeNode(game['title'])

            # iterate over tags and insert to tree
            for tag in game['tags']:
                tag_node = tree.search(tag)
                if tag_node is None:
                    tag_node = BinarySearchTreeNode(tag)
                    tree.insert(tag_node)
                tag_node.insert(game_node)

            # iterate over platforms and insert to tree
            for platform in game['platforms']:
                platform_node = tree.search(platform)
                if platform_node is None:
                    platform_node = BinarySearchTreeNode(platform)
                    tree.insert(platform_node)
                platform_node.insert(game_node)

            # Insert game to the tree of ratings
            rating_node = tree.search('Rating')
            if rating_node is None:
                rating_node = BinarySearchTreeNode('Rating')
                tree.insert(rating_node)
            rating_node.insert(game_node)

            # Insert game to the tree of ESRB Ratings
            esrb_rating_node = tree.search('ESRB Rating')
            if esrb_rating_node is None:
                esrb_rating_node = BinarySearchTreeNode('ESRB Rating')
                tree.insert(esrb_rating_node)
            esrb_rating_node.insert(game_node)

            # Insert game to the tree of Release Dates
            release_date_node = tree.search('Release Date')
            if release_date_node is None:
                release_date_node = BinarySearchTreeNode('Release Date')
                tree.insert(release_date_node)
            release_date_node.insert(game_node)

        return tree
