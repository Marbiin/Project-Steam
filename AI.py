import json

def load_games_data():
    with open("steam.json", "r") as file:
        games_data = json.load(file)
    return games_data

def most_frequent_genre():
    games_data = load_games_data()
    genre_count = {}
    for game in games_data:
        genres = game.get("genres", "")
        if genres:
            for genre in genres.split(","):
                genre = genre.strip()
                genre_count[genre] = genre_count.get(genre, 0) + 1

    most_common_genre = max(genre_count, key=genre_count.get)
    return most_common_genre, genre_count[most_common_genre]

def price_spread():
    games_data = load_games_data()
    prices = [game.get("price", 0) for game in games_data if game.get("price", 0) > 0]

    mean_price = sum(prices) / len(prices) if prices else 0
    squared_differences = [(price - mean_price) ** 2 for price in prices]
    variance = sum(squared_differences) / len(prices) if prices else 0
    spread = variance ** 0.5

    return spread

def predict_playtime(price, price_range=2):
    games_data = load_games_data()
    filtered_games = [
        game for game in games_data
        if "price" in game and "average_playtime" in game and
        game["price"] >= (price - price_range) and game["price"] <= (price + price_range)
    ]
    if not filtered_games:
        return 0

    total_playtime = sum(game["average_playtime"] for game in filtered_games)
    average_playtime = total_playtime / len(filtered_games)

    return average_playtime
