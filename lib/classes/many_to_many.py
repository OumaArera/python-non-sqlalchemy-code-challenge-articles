# Author class
class Author:
    def __init__(self, name):
        # Check if the provided name is a non-empty string
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Invalid name for author")
        # Initialize author with a name and an empty list to store articles
        self._name = name
        self._articles = []

    @property
    def name(self):
        # Getter method for the author's name
        return self._name

    def articles(self):
        # Getter method for the list of articles written by the author
        return self._articles

    def magazines(self):
        # Getter method for the list of unique magazines the author has contributed to
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Check if an article with the same magazine and title already exists for the author
        existing_articles = [article for article in self._articles if article.magazine == magazine and article.title == title]
        
        if existing_articles:
            # If it exists, return the existing article
            return existing_articles[0]
        
        # If it doesn't exist, create a new article and append it to the author's articles list
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        # Get a list of unique topic areas (magazine categories) the author has contributed to
        return list(set(article.magazine.category for article in self._articles)) if self._articles else None


# Magazine class
class Magazine:
    def __init__(self, name, category):
        # Check if the provided name is a string with length between 2 and 16 characters
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Invalid name for magazine")
        # Check if the provided category is a non-empty string
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Invalid category for magazine")
        # Initialize magazine with a name, category, and an empty list to store articles
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        # Getter method for the magazine's name
        return self._name

    @property
    def category(self):
        # Getter method for the magazine's category
        return self._category

    def articles(self):
        # Getter method for the list of articles published in the magazine
        return self._articles

    def contributors(self):
        # Getter method for the list of unique authors who have contributed to the magazine
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        # Getter method for a list of article titles published in the magazine
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        # Get a list of authors who have contributed more than 2 articles to the magazine
        author_count = {}
        for article in self._articles:
            author_count[article.author] = author_count.get(article.author, 0) + 1
        return [author for author, count in author_count.items() if count > 2]
    
    @classmethod
    def top_publisher(cls):
        # Class method to find the magazine with the most articles
        if not Article.all:
            # If there are no articles, return None
            return None

        magazine_article_counts = {}
        for article in Article.all:
            # Count the number of articles for each magazine
            magazine_article_counts[article.magazine] = magazine_article_counts.get(article.magazine, 0) + 1

        if not magazine_article_counts:
            # If there are no magazine-article associations, return None
            return None

        # Find the magazine with the maximum number of articles
        top_magazine = max(magazine_article_counts, key=magazine_article_counts.get)
        return top_magazine


class Article:
    # Class attribute to keep track of all created instances of Article
    all = []

    def __init__(self, author, magazine, title):
        # Check if the provided title is a string with length between 5 and 50 characters
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Invalid title for article")
        # Initialize an article with an author, magazine, and title
        self._author = author
        self._magazine = magazine
        self._title = title
        # Append the article to the author's and magazine's articles lists
        author.articles().append(self)
        magazine.articles().append(self)

        # Add the created instance to the class attribute tracking all articles
        Article.all.append(self)

    @property
    def title(self):
        # Getter method for the article's title
        return self._title

    @property
    def author(self):
        # Getter method for the article's author
        return self._author

    @property
    def magazine(self):
        # Getter method for the article's magazine
        return self._magazine
