from abc import ABC, abstractmethod
from datetime import datetime

class Movie_Abstract(ABC):
    @abstractmethod
    def text_file(self):
        """
        Abstract method to be implemented by subclasses to return a string representation of the movie.
        """
        pass


class BaseFilm(Movie_Abstract):
    """
    Base class for all film-related objects. Contains common attributes and methods for both movies and shows.
    """

    def __init__(self, id, title, genre, producer, release_date, number_of_views, average_rating, director,
                 age_restrictions, duration, types, episodes):
        """
        Initializes a base film object with provided attributes.

        Args:
            id (str): Unique identifier for the movie/show.
            title (str): Title of the movie/show.
            genre (str): Genre of the movie/show.
            producer (str): Producer of the movie/show.
            release_date (str): Release date of the movie/show in YYYY-MM-DD format.
            number_of_views (int): Number of views the movie/show has.
            average_rating (float): Average rating of the movie/show.
            director (str): Director of the movie/show.
            age_restrictions (str): Age restrictions for the movie/show.
            duration (int): Duration of the movie/show in minutes.
            types (str): Type of the film, either 'Movie' or 'Show'.
            episodes (str): Number of episodes for a show. For movies, it will be '-'.
        """
        self.__id = id
        self.__title = title
        self.__genre = genre
        self.__duration = duration
        self.__producer = producer
        self.__release_date = release_date
        self.__number_of_views = number_of_views
        self.__average_rating = average_rating
        self.__director = director
        self.__age_restrictions = age_restrictions
        self.__type = types
        self.__episodes = episodes

    def text_file(self):
        """
        Returns a textual representation of the movie/show's details.

        Returns:
            str: A formatted string containing the details of the movie/show.
        """
        return (
            f"ID: {self.get_id()}\n"
            f"Title: {self.get_movie_title()}\n"
            f"Genre: {self.get_genre()}\n"
            f"Duration: {self.get_duration()}\n"
            f"Producer: {self.get_producer()}\n"
            f"Release Date: {self.get_release_date()}\n"
            f"Number of Views: {self.get_number_of_views()}\n"
            f"Average Rating: {self.get_average_rating()}\n"
            f"Director: {self.get_director()}\n"
            f"Age Restriction: {self.get_age_restrictions()}\n"
            f"Type: {self.get_type()}\n"
            f"Episodes: {self.get_episodes()}\n"
        )

    def get_id(self):
        """
        Returns the ID of the movie/show.

        Returns:
            str: The ID of the movie/show.
        """
        return self.__id

    def set_id(self, id):
        """
        Sets a new ID for the movie/show.

        Args:
            id (str): The new ID for the movie/show.
        """
        self.__id = id

    def get_movie_title(self):
        """
        Returns the title of the movie/show.

        Returns:
            str: The title of the movie/show.
        """
        return self.__title

    def set_movie_title(self, movie_title):
        """
        Sets a new title for the movie/show.

        Args:
            movie_title (str): The new title for the movie/show.
        """
        self.__title = movie_title

    def get_average_rating(self):
        """
        Returns the average rating of the movie/show.

        Returns:
            float: The average rating of the movie/show.
        """
        return self.__average_rating

    def set_movie_rating(self, new_rating):
        """
        Sets a new average rating for the movie/show.

        Args:
            new_rating (float): The new average rating for the movie/show.

        Raises:
            ValueError: If the rating is not between 0 and 10.
        """
        if 0 <= new_rating <= 10:
            self.__average_rating = new_rating
        else:
            raise ValueError("Average rating must be between 0 and 10.")

    def get_genre(self):
        """
        Returns the genre of the movie/show.

        Returns:
            str: The genre of the movie/show.
        """
        return self.__genre

    def get_producer(self):
        """
        Returns the producer of the movie/show.

        Returns:
            str: The producer of the movie/show.
        """
        return self.__producer

    def get_release_date(self):
        """
        Returns the release date of the movie/show.

        Returns:
            str: The release date of the movie/show in YYYY-MM-DD format.
        """
        return self.__release_date

    def get_number_of_views(self):
        """
        Returns the number of views for the movie/show.

        Returns:
            int: The number of views for the movie/show.
        """
        return self.__number_of_views

    def get_director(self):
        """
        Returns the director of the movie/show.

        Returns:
            str: The director of the movie/show.
        """
        return self.__director

    def get_age_restrictions(self):
        """
        Returns the age restriction of the movie/show.

        Returns:
            str: The age restriction of the movie/show.
        """
        return self.__age_restrictions

    def get_duration(self):
        """
        Returns the duration of the movie/show.

        Returns:
            int: The duration of the movie/show in minutes.
        """
        return self.__duration

    def get_type(self):
        """
        Returns the type of the film (Movie/Show).

        Returns:
            str: The type of the film, either 'Movie' or 'Show'.
        """
        return self.__type

    def get_episodes(self):
        """
        Returns the number of episodes (for Shows).

        Returns:
            str: The number of episodes or '-' for Movies.
        """
        return self.__episodes


class Movies(BaseFilm):
    """
    Subclass representing a movie. Inherits from BaseFilm and implements its functionality.
    """

    def __init__(self, id, title, genre, producer, release_date, number_of_views, average_rating, director,
                 age_restrictions, duration):
        """
        Initializes a movie object by passing attributes to the parent class.

        Args:
            id (str): Unique identifier for the movie.
            title (str): Title of the movie.
            genre (str): Genre of the movie.
            producer (str): Producer of the movie.
            release_date (str): Release date of the movie.
            number_of_views (int): Number of views the movie has.
            average_rating (float): Average rating of the movie.
            director (str): Director of the movie.
            age_restrictions (str): Age restriction for the movie.
            duration (int): Duration of the movie in minutes.
        """
        episodes = '-'
        super().__init__(id, title, genre, producer, release_date, number_of_views, average_rating, director,
                         age_restrictions, duration, "Movie", episodes)


class Shows(BaseFilm):
    """
    Subclass representing a show. Inherits from BaseFilm and implements its functionality.
    """

    def __init__(self, id, title, genre, producer, release_date, number_of_views, average_rating, director,
                 age_restrictions, duration, episodes):
        """
        Initializes a show object by passing attributes to the parent class.

        Args:
            id (str): Unique identifier for the show.
            title (str): Title of the show.
            genre (str): Genre of the show.
            producer (str): Producer of the show.
            release_date (str): Release date of the show.
            number_of_views (int): Number of views the show has.
            average_rating (float): Average rating of the show.
            director (str): Director of the show.
            age_restrictions (str): Age restriction for the show.
            duration (int): Duration of the show in minutes.
            episodes (int): Number of episodes in the show.
        """
        super().__init__(id, title, genre, producer, release_date, number_of_views, average_rating, director,
                         age_restrictions, duration, "Show", episodes)


class Movie_observer(ABC):
    """
    Abstract base class for movie observers. All concrete observers must implement the update_viewer and update_observer methods.
    """

    @abstractmethod
    def update_viewer(self, movie, action):
        """
        Method to notify viewers about a change in the movie (e.g., new movie, rating update, movie deletion).

        Parameters:
            movie: The movie that was updated.
            action: The type of action (e.g., add, update, delete).
        """
        pass

    @abstractmethod
    def update_observer(self, movie, action):
        """
        Method to notify other observers (e.g., database updates) about the change in the movie.

        Parameters:
            movie: The movie that was updated.
            action: The type of action (e.g., add, update, delete).
        """
        pass


class Observer_Notification(Movie_observer):
    """
    Concrete observer that handles notifications to viewers and other observers.
    """

    def update_viewer(self, movie, action):
        """
        Notifies the viewer about the action performed on the movie.

        Parameters:
            movie: The movie that was updated.
            action: The action to notify about (1 = added, 2 = rating updated, 5 = deleted).
        """
        print()
        if action == 1:
            print(f"Viewer Notification: A new movie '{movie.get_movie_title()}' has been added!")
        elif action == 2:
            print(f"Viewer Notification: Movie '{movie.get_movie_title()}' rating has been updated!")
        elif action == 5:
            print(f"Viewer Notification: Movie '{movie.get_movie_title()}' has been deleted!")

    def update_observer(self, movie, action):
        """
        Notifies the observer about the action performed on the movie.

        Parameters:
            movie: The movie that was updated.
            action: The action to notify about (e.g., check database for update).
        """
        print()
        print(f"Observer Update: Action {action} performed. Check the database!")


class Movie_Manager:
    """
    Manages a collection of movies, including adding, removing, and updating movies. It also allows searching and saving the movie list to a file.
    """

    def __init__(self, filename):
        """
        Initializes the Movie Manager with a filename to load and save movies.

        Parameters:
            filename: The file from which movie data is loaded and saved.
        """
        self.__filename = filename
        self.__movies = []
        self.__observers = []
        self.load_movies()

    def add_observer(self, observer):
        """
        Adds an observer to the list of observers for notifications.

        Parameters:
            observer: The observer to be added.
        """
        self.__observers.append(observer)

    def notify_observer(self, movie, action):
        """
        Notifies all observers about a change to a movie.

        Parameters:
            movie: The movie that was updated.
            action: The type of action performed on the movie (e.g., add, update, delete).
        """
        for observer in self.__observers:
            observer.update_viewer(movie, action)
            observer.update_observer(movie, action)

    def load_movies(self):
        """
        Loads movie data from the specified file. If the file doesn't exist, creates an empty one.
        """
        try:
            with open(self.__filename, "r") as file:
                contents_of_file = file.read().strip()
                movie_data = contents_of_file.split("\n\n")
                for movie in movie_data:
                    lines = movie.split("\n")
                    data = {}
                    for line in lines:
                        if ": " in line:
                            key, value = line.split(": ", 1)
                            data[key] = value.strip()

                    if all(key in data for key in ['ID', 'Title', 'Genre', 'Duration', 'Producer', 'Release Date',
                                                   'Number of Views', 'Average Rating', 'Director', 'Age Restriction',
                                                   'Type']):
                        if data["Type"] == "Movie":
                            movie_obj = Movies(
                                id=data["ID"],
                                title=data["Title"],
                                genre=data["Genre"],
                                duration=int(data["Duration"]),
                                producer=data["Producer"],
                                release_date=data["Release Date"],
                                number_of_views=int(data["Number of Views"]),
                                average_rating=float(data["Average Rating"]),
                                director=data["Director"],
                                age_restrictions=data["Age Restriction"]
                            )

                        elif data["Type"] == "Show":
                            movie_obj = Shows(
                                id=data["ID"],
                                title=data["Title"],
                                genre=data["Genre"],
                                duration=int(data["Duration"]),
                                producer=data["Producer"],
                                release_date=data["Release Date"],
                                number_of_views=int(data["Number of Views"]),
                                average_rating=float(data["Average Rating"]),
                                director=data["Director"],
                                age_restrictions=data["Age Restriction"],
                                episodes=int(data["Episodes"])
                            )
                        self.__movies.append(movie_obj)

        except FileNotFoundError:
            print("File doesn't exist. Creating an empty file.")
            open(self.__filename, "w").close()

        except Exception as e:
            print(f"Error while loading movies: {e}")

    def save_movies(self):
        """
        Saves the current list of movies to the file.
        """
        try:
            with open(self.__filename, "w") as file:
                for movie in self.__movies:
                    file.write(movie.text_file() + "\n")

        except Exception as e:
            print(f"Error while saving movies: {e}")

    def search_movies(self):
        """
        Allows the user to search for movies by title or genre and displays the results.
        """
        while True:
            search_criteria = input("\nSearch by (1) Title or (2) Genre? (Enter 1 or 2, or 'quit' to exit): ").lower()
            if search_criteria == "1":
                search_input = input("Enter the title to search for: ").strip().lower()
                results = [movie for movie in self.__movies if search_input in movie.get_movie_title().lower()]
            elif search_criteria == "2":
                search_input = input("Enter the genre to search for: ").strip().lower()
                results = [movie for movie in self.__movies if search_input in movie.get_genre().lower()]
            elif search_criteria == "quit":
                print("Exiting search.")
                break
            else:
                print("Invalid input! Please enter 1, 2, or 'quit'.")
                continue

            if results:
                print("\n--- Search Results ---")
                for movie in results:
                    print(movie.text_file())
            else:
                print("No results found. Try again.")

    def add_movie_from_input(self):
        """
        Prompts the user to input information about a new movie and adds it to the list.
        """
        while True:
            id = input("Enter Movie ID: ")
            if any(movie.get_id() == id for movie in self.__movies):
                print("ID already exists!")
                continue
            break

        # INPUT TITLE
        while True:
            title = input("Enter Title: ").strip()
            new_title = title.lower()

            if any(movie.get_movie_title().strip().lower() == new_title for movie in self.__movies):
                print("Title already exists!")
                continue
            break

        # INPUT GENRE
        genre = input("Enter Genre: ")

        # INPUT DURATION
        while True:
            try:
                duration = int(input("Enter Duration (in minutes): "))
                if duration <= 0:
                    print("Duration must be a positive number!")
                    continue

            except ValueError:
                print("Invalid input for duration!")
                continue
            break

        # INPUT PRODUCER
        producer = input("Enter Producer: ")

        # INPUT RELEASE DATE
        while True:
            release_date = input("Enter Release Date (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(release_date, "%Y-%m-%d")
            except ValueError:
                print("Invalid date format! Please use 'YYYY-MM-DD'.")
                continue
            break

        # INPUT NUMBER OF VIEWS
        while True:
            try:
                number_of_views = int(input("Enter Number of Views: "))
                if number_of_views < 0:
                    print("Number of views must not be negative.")
                    continue
            except ValueError:
                print("Invalid input for number of views! Please enter a number.")
                continue
            break

        # INPUT AVERAGE RATING
        while True:
            try:
                average_rating = float(input("Enter Average Rating (0-10): "))
                if not (0 <= average_rating <= 10):
                    print("Average rating must be between 0 and 10!")
                    continue
            except ValueError:
                print("Invalid input for average rating! Please enter a number.")
                continue
            break

        # INPUT DIRECTOR
        director = input("Enter Director: ")

        # INPUT AGE RESTRICTIONS
        while True:
            age_restrictions = input("Enter Age Restriction (PG-13, R, 18+, 21+): ").strip()
            if age_restrictions not in ["PG-13", "R", "18+", "21+"]:
                print("Invalid age restriction! Please choose from 'PG-13', 'R', '18+', or '21+'.")
                continue
            break

        # INPUT TYPE (MOVIE OR SHOW)
        while True:
            type_of_movie = input("Enter Type (Movie or Show): ").capitalize()
            if type_of_movie not in ["Movie", "Show"]:
                print("Invalid type! Please choose either 'Movie' or 'Show'.")
                continue
            break

        if type_of_movie == "Movie":
            new_movie = Movies(
                id=id,
                title=title,
                genre=genre,
                producer=producer,
                release_date=release_date,
                number_of_views=number_of_views,
                average_rating=average_rating,
                director=director,
                age_restrictions=age_restrictions,
                duration=duration
            )

        else:
            try:
                episodes = int(input("Enter Number of Episodes: "))
                if episodes < 1:
                    print("Episodes must be at least 1!")
                    return

            except ValueError:
                print("Invalid input for episodes!")
                return

            new_movie = Shows(
                id=id,
                title=title,
                genre=genre,
                producer=producer,
                release_date=release_date,
                number_of_views=number_of_views,
                average_rating=average_rating,
                director=director,
                age_restrictions=age_restrictions,
                duration=duration,
                episodes=episodes
            )

        self.__movies.append(new_movie)
        self.save_movies()
        self.notify_observer(new_movie, 1)
        print(f"Movie/Show '{title}' added successfully!")

    def update_movie_rating(self, id, new_rating):
        """
        Updates the rating of an existing movie/show.

        Parameters:
            id: The ID of the movie/show to update.
            new_rating: The new rating for the movie/show (between 0 and 10).
        """
        try:
            if not (0 <= new_rating <= 10):
                raise ValueError("Average rating must be between 0 and 10.")

            for movie in self.__movies:
                if movie.get_id() == id:
                    movie.set_movie_rating(new_rating)
                    self.notify_observer(movie, 2)
                    self.save_movies()
                    print(f"Rating for Movie/Show '{movie.get_movie_title()}' updated to {new_rating}.")
                    return
            print(f"No movie/show found with ID '{id}'.")

        except ValueError as e:
            print(f"Error: {e}")

    def remove_movie(self, id):
        """
        Removes a movie/show from the list.

        Parameters:
            id: The ID of the movie/show to remove.
        """
        try:
            for movie in self.__movies:
                if movie.get_id() == id:
                    self.__movies.remove(movie)
                    self.save_movies()
                    print(f"Movie/Show '{movie.get_movie_title()}' has been deleted.")
                    self.notify_observer(movie, 4)
                    return
            print(f"Movie/Show with ID '{id}' not found.")

        except Exception as e:
            print(f"Error: {e}")

    def list_movies(self):
        """
        Lists all movies with pagination.
        """
        page = 1
        items_per_page = 10
        total_pages = (len(self.__movies) + items_per_page - 1) // items_per_page

        while True:
            print(f"\n--- List of Movies (Page {page}/{total_pages}) ---")
            movies = [movie for movie in self.__movies if movie.get_type() == "Movie"]
            start = (page - 1) * items_per_page
            end = start + items_per_page
            for movie in movies[start:end]:
                print(movie.text_file())

            if total_pages == 1:
                break

            choose = input("\nEnter 'next' for next page, 'prev' for previous page, or 'quit' to quit: ").lower()
            if choose == "next" and page < total_pages:
                page += 1
            elif choose == "prev" and page > 1:
                page -= 1
            elif choose == "quit":
                break
            else:
                print("Invalid input. Please try again.")

    def list_shows(self):
        """
        Lists all shows with pagination.
        """
        page = 1
        items_per_page = 10
        total_pages = (len(self.__movies) + items_per_page - 1) // items_per_page

        while True:
            print(f"\n--- List of Shows (Page {page}/{total_pages}) ---")
            shows = [movie for movie in self.__movies if movie.get_type() == "Show"]
            start = (page - 1) * items_per_page
            end = start + items_per_page
            for movie in shows[start:end]:
                print(movie.text_file())

            if total_pages == 1:
                break

            choose = input("\nEnter 'next' for next page, 'prev' for previous page, or 'quit' to quit: ").lower()
            if choose == "next" and page < total_pages:
                page += 1
            elif choose == "page" and page > 1:
                page -= 1
            elif choose == "quit":
                break
            else:
                print("Invalid input. Please try again.")
                
#MAIN FUNCTION
manager = Movie_Manager("movies_data.txt")
observer = Observer_Notification()
manager.add_observer(observer)

while True:
    print("\n--- Movie Manager ---")
    print("1. Add Movie/Show from Input")
    print("2. Update Movie/Show Rating")
    print("3. List Movies")
    print("4. List Shows")
    print("5. Remove Movie/Show")
    print("6. Search Movies/Shows")
    print("7. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        manager.add_movie_from_input()

    elif choice == "2":
        id = input("Enter Movie/Show ID to update rating: ")
        new_rating = float(input("Enter new rating (0-10): "))
        manager.update_movie_rating(id, new_rating)

    elif choice == "3":
        manager.list_movies()

    elif choice == "4":
        manager.list_shows()

    elif choice == "5":
        id = input("Enter Movie/Show ID to remove: ")
        manager.remove_movie(id)

    elif choice == "6":
        manager.search_movies()

    elif choice == "7":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

