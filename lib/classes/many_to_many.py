# Author class
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Invalid name for author")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    # def add_article(self, magazine, title):
    #     new_article = Article(self, magazine, title)
    #     self._articles.append(new_article)
    #     return new_article

    def add_article(self, magazine, title):
        # Check if an article with the same magazine and title already exists
        existing_articles = [article for article in self._articles if article.magazine == magazine and article.title == title]
        
        if existing_articles:
            # If it exists, return the existing article
            return existing_articles[0]
        
        # If it doesn't exist, create a new article and append it to the list
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles)) if self._articles else None


# Magazine class
class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Invalid name for magazine")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Invalid category for magazine")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            author_count[article.author] = author_count.get(article.author, 0) + 1
        return [author for author, count in author_count.items() if count > 2]
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None

        magazine_article_counts = {}
        for article in Article.all:
            magazine_article_counts[article.magazine] = magazine_article_counts.get(article.magazine, 0) + 1

        if not magazine_article_counts:
            return None

        top_magazine = max(magazine_article_counts, key=magazine_article_counts.get)
        return top_magazine


class Article:
    # Class attribute to keep track of all created instances
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Invalid title for article")
        self._author = author
        self._magazine = magazine
        self._title = title
        author.articles().append(self)
        magazine.articles().append(self)

        # Add the created instance to the class attribute
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

