from models import Session, Restaurant, Orders
from datetime import datetime
session = Session()
# 4 - create movies

kilala = Restaurant('Kilala')
sushi_town = Restaurant('Sushi_Town')
food = Restaurant('Food')

order1 = Orders(1, datetime.now(), datetime.now())


# 9 - persists data
session.add(order1)
session.add(kilala)
session.add(sushi_town)
session.add(food)

# 10 - commit and close session
session.commit()
session.close()