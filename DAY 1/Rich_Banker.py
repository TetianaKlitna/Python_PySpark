import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Option 1
randomFriendInd = random.randint(0, len(friends) - 1)
print(friends[randomFriendInd])
# Option 2
print(random.choice(friends))
