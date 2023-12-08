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
                tags = [tag.get('name', 'N/A') for tag in game.get('tags', []) if tag.get('language', 'N/A') == 'eng']
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

    # Create nodes for each attribute
    platform_node = BinarySearchTreeNode('Platforms')
    rating_node = BinarySearchTreeNode('Rating')
    esrb_rating_node = BinarySearchTreeNode('ESRB Rating')
    tags_node = BinarySearchTreeNode('Tags')
    release_date_node = BinarySearchTreeNode('Release Date')
    screenshots_node = BinarySearchTreeNode('Screenshots')

    # Add attribute nodes to game node
    game_node.add_child(platform_node)
    game_node.add_child(rating_node)
    game_node.add_child(esrb_rating_node)
    game_node.add_child(tags_node)
    game_node.add_child(release_date_node)
    game_node.add_child(screenshots_node)

    # Add specific elements as child nodes to the attribute nodes

    # Platforms
    for platform in game['platforms']:
        specific_platform_node = BinarySearchTreeNode(platform)
        platform_node.add_child(specific_platform_node)
    
    # Rating
    specific_rating_node = BinarySearchTreeNode(str(game['rating']))
    rating_node.add_child(specific_rating_node)

    # ESRB Rating
    specific_esrb_rating_node = BinarySearchTreeNode(str(game['esrb_rating']))
    esrb_rating_node.add_child(specific_esrb_rating_node)

    # Tags
    for tag in game['tags']:
        specific_tag_node = BinarySearchTreeNode(tag)
        tags_node.add_child(specific_tag_node)

    # Release Date
    specific_release_date_node = BinarySearchTreeNode(game['release_date'])
    release_date_node.add_child(specific_release_date_node)

    # Screenshots
    for screenshot in game['screenshots']:
        specific_screenshot_node = BinarySearchTreeNode(screenshot)
        screenshots_node.add_child(specific_screenshot_node)




## Test tree
'''
def test_tree():
    for game in game_nodes:
        print(game.name)

test_tree()

def print_tree(node, level=0):
    print(' ' * level  + '-' * level + '> ' + node.name)
    for child in node.children:
        print_tree(child, level + 1)

for game_node in game_nodes:
    print_tree(game_node)
'''