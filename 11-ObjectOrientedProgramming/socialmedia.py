class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f'{self.username} posts timeline:')
        print(f'{self.posts}')

johndoe = SocialMediaProfile('johndoe')
johndoe.add_post ='Hello, world!'
johndoe.add_post = 'had a great day at the park :>'
johndoe.add_post ="What's up, Natalie? How are you?"
johndoe.display_timeline()