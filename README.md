Project Title: Movie and Show Management System

Description:
- A Movie and Show Management System designed using Object-Oriented Programming (OOP) principles in Python.
- The system enables users to add, update, search, and remove movies and shows, with a built-in notification system using the Observer Design Pattern.
- The project demonstrates the integration of OOP concepts such as encapsulation, inheritance, and polymorphism to build a scalable and maintainable system.

Key Features:
1. Movie/Show Management:
   Add, update, and delete movies and shows, with all necessary attributes like title, genre, duration, and more.
   Movies and shows are treated as objects, leveraging OOP principles for flexibility and reuse.
   Supports additional show-specific features such as episodes.

2. Search Functionality:
   Users can search movies and shows by title or genre, improving user experience by filtering through large collections.
   Search results are displayed in an easy-to-read format.

3. Observer Pattern:
   Observers (e.g., viewers and administrators) are notified of updates, such as when a movie/show is added, updated, or deleted.
   Implementing the observer design pattern ensures real-time notifications, enhancing the responsiveness of the system.

4. Pagination:
   Movies and shows are displayed in pages, with the option to navigate between pages, improving usability for large datasets.

5. User Interface:
   Command-line interface (CLI) where users can interact with the system, perform CRUD operations on movies and shows, and receive notifications.

Technical Highlights:

- Object-Oriented Programming (OOP):
  The system makes use of OOP principles like inheritance (e.g., Movies and Shows as subclasses), encapsulation (storing data within objects), and polymorphism (e.g., handling different types of notifications for viewers and administrators).
  The structure makes it easy to expand the system in the future, such as by adding new features or integrating external services.

- Observer Design Pattern:
  Real-time updates are sent to observers whenever there is a change to the movie or show data.
  Viewer notifications keep users informed about changes like new movies or updated ratings.
  Admin notifications ensure that the system is in sync with backend changes, such as when a movie/show is added or deleted.
