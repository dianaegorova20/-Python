class Table:
    """
    Abstract class representing a table.

    Attributes:
        material (str): The material of the table (e.g., wood, metal).
        legs (int): The number of legs the table has.

    Methods:
        clean_surface(self) -> None:
            Clean the surface of the table.

        adjust_height(self, new_height: float) -> None:
            Adjust the height of the table.

        calculate_capacity(self, load: float) -> float:
            Calculate the maximum load capacity of the table.

    """

    def __init__(self, material: str, legs: int):
        """
        Initialize a Table object.

        Args:
            material (str): The material of the table.
            legs (int): The number of legs the table has.

        Raises:
            ValueError: If the number of legs is not a positive integer.
        """
        if not isinstance(legs, int) or legs <= 0:
            raise ValueError("Number of legs must be a positive integer.")
        self.material = material
        self.legs = legs

    def clean_surface(self) -> None:
        ...

    def adjust_height(self, new_height: float) -> None:
        ...

    def calculate_capacity(self, load: float) -> float:
        ...


class Tree:
    """
    Abstract class representing a tree.

    Attributes:
        species (str): The species of the tree.
        height (float): The height of the tree in meters.

    Methods:
        grow(self, growth_rate: float) -> None:
            Simulate the growth of the tree.

        shed_leaves(self, season: str) -> None:
            Shed leaves based on the season.

        get_age(self) -> int:
            Get the age of the tree in years.

    """

    def __init__(self, species: str, height: float):
        """
        Initialize a Tree object.

        Args:
            species (str): The species of the tree.
            height (float): The height of the tree.

        Raises:
            ValueError: If height is not a positive number.
        """
        if height <= 0:
            raise ValueError("Height must be a positive number.")
        self.species = species
        self.height = height

    def grow(self, growth_rate: float) -> None:
        ...

    def shed_leaves(self, season: str) -> None:
        ...

    def get_age(self) -> int:
        ...


class SocialMediaPlatform:
    """
    Abstract class representing a social media platform.

    Attributes:
        name (str): The name of the social media platform.
        user_count (int): The number of users on the platform.

    Methods:
        create_account(self, username: str, password: str) -> None:
            Create a new user account on the platform.

        post_content(self, content: str) -> str:
            Post content on the platform.

        analyze_engagement(self) -> float:
            Analyze the engagement level on the platform.

    """

    def __init__(self, name: str, user_count: int):
        """
        Initialize a SocialMediaPlatform object.

        Args:
            name (str): The name of the social media platform.
            user_count (int): The initial number of users on the platform.

        Raises:
            ValueError: If user_count is not a positive integer.
        """
        if not isinstance(user_count, int) or user_count <= 0:
            raise ValueError("User count must be a positive integer.")
        self.name = name
        self.user_count = user_count

    def create_account(self, username: str, password: str) -> None:
        ...

    def post_content(self, content: str) -> str:
        ...

    def analyze_engagement(self) -> float:
        ...