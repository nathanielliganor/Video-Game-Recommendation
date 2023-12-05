import requests
import json
import os

search_term = input('Enter a search term: ')

api_key = "27f9898959fa47b59eadb89d4ff0b71b"
url = f'https://api.rawg.io/api/games?key={api_key}&search={search_term}'

game_data_list = []

cache_file = f"cache/{search_term}.json"
if os.path.exists(cache_file):
    with open(cache_file, "r") as f:
        game_data_list = json.load(f)

else:
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            games = data.get('results', [])

            for game in games:
                title = game.get('name', 'N/A')
                platforms = game.get('platforms', [])
                names_list = [platform_info['platform']['name'] for platform_info in platforms]
                rating = game.get('rating', 'N/A')
                esrb_rating = game.get('esrb_rating', {}).get('name', 'N/A')
                tags = [tag.get('name', 'N/A') for tag in game.get('tags', [])]
                release_date = game.get('released', 'N/A')
                screenshots = [screenshot.get('image', 'N/A') for screenshot in game.get('short_screenshots', [])]
                
                '''
                print(f'Title: {title}')
                print(f'Platforms: {names_list}')
                print(f'Rating: {rating}')  
                print(f'ESRB Rating: {esrb_rating}')
                print(f'Tags: {tags}')
                print(f'Release Date: {release_date}')
                print('Screenshots:')
                for screenshot in screenshots:
                    print(f' - {screenshot}')
                print('-' * 30)
                '''

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

            # Save data to cache
            with open(cache_file, "w") as f:
                json.dump(game_data_list, f)

        else:
            print(f'Error: {response.status_code}')
    except Exception as e:
        print(f'Error: {e}')

#print(game_data_list)

# STEP 4: DATA PROCESSING AND ORGANIZATION

class BinarySearchTreeNode:

    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    
    def search(self, name):
        if self.name == name:
            return self
        
        for child in self.children:
            result = child.search(name)
            if result is not None:
                return result
        
        return None

game_nodes = []

root_node = BinarySearchTreeNode('Video Games')

for game in game_data_list:
    game_node = BinarySearchTreeNode(game['title'])
    game_nodes.append(game_node)

    '''
    # Add genre to the game node
    for genre in game['genre']:
        genre_node = BinarySearchTreeNode(genre)
        game_node.add_child(genre_node, relation="genre")
    '''
        
    # Add platform to the game node
    for platform in game['platforms']:
        platform_node = BinarySearchTreeNode(platform)
        game_node.add_child(platform_node)
    
    # Add rating to the game node
        rating = str(rating)
        rating_node = BinarySearchTreeNode(rating)
        game_node.add_child(rating_node)
    
    # Add esrb rating to the game node
    for esrb_rating in game['esrb_rating']:
        esrb_rating_node = BinarySearchTreeNode(esrb_rating)
        game_node.add_child(esrb_rating_node)

    # Add tags to the game node
    for tag in game['tags']:
        tag_node = BinarySearchTreeNode(tag)
        game_node.add_child(tag_node)

    # Add release date to the game node
    for release_date in game['release_date']:
        release_date_node = BinarySearchTreeNode(release_date)
        game_node.add_child(release_date_node)
    
    # Add screenshots to the game node
    for screenshot in game['screenshots']:
        screenshot_node = BinarySearchTreeNode(screenshot)
        game_node.add_child(screenshot_node)

## Test tree
def test_tree():
    for game in game_nodes:
        print(game.name)

test_tree()

def print_tree(node, level=0):
    print(' ' * level + node.name)
    for child in node.children:
        print_tree(child, level + 1)

print_tree(game_node)