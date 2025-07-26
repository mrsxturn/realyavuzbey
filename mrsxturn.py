class MrSxturn:
    def __init__(self):
        self.name = "Yavuz"
        self.location = "Türkiye"
        self.role = "Full-Stack Developer & Entrepreneur"
        self.main_stack = ["Python", "Flask", "SQLAlchemy"]
        self.interests = [
            "C#", "CSS3", "Git", "HTML5", "Linux",
            "MariaDB", "MySQL", "PHP", "Python"
        ]
        self.socials = {
            "Twitter": "https://twitter.com/mrsxturn"
        }

    def intro(self):
        return (
            f"My name is {self.name}. I am a {self.role} based in {self.location}.\n"
            f"I work mostly with {self.main_stack[0]}, especially {self.main_stack[1]}, "
            f"and I prefer building clean, functional systems with {self.main_stack[2]} and other tools."
        )

    def get_interests(self):
        return f"Technologies I've explored or actively use: {', '.join(self.interests)}"

    def connect(self):
        return f"Find me on Twitter: {self.socials['Twitter']}"

    def __str__(self):
        return f"{self.intro()}\n\n{self.get_interests()}\n\n{self.connect()}"


if __name__ == "__main__":
    profile = MrSxturn()
    print(profile)
