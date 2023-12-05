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

