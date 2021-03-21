from datetime import datetime
import sqlite3


# helper functions
def getTimestamp(alternativeDate=None):
    """ Returns the timestamp of the date passed in or the time this method is executed"""
    now = alternativeDate or datetime.now()
    return datetime.timestamp(now)


currentMoneyNotification = "The foundation has committed to giving $250 million for Covid-19 vaccination development and distribution"
previousMoneyNotification = "The foundation has committed to $1.75 billion for Covid-19 vaccination development and distribution"
currentFirstVaccineNotification = "19.9% of the American population have received at least one dose of the vaccine"
currentSecondVaccineNotification = '10.3% of the American population are fully vaccinated'
previousFirstVaccineNotification = "11.7% of the American population have received at least one dose of the vaccine"
previousSecondVaccineNotification = '5.6% of the American population are fully vaccinated'

# creating the sqLite notification database
print("Create a notifications database...")

conn = sqlite3.connect('notifications.db')  # creates notifications store
conn.execute("CREATE TABLE notifications (category char(50), notification char(1000), timestamp int(50), id INTEGER "
             "PRIMARY KEY )")
# current money notification
conn.execute(
    "INSERT INTO notifications (category, notification, timestamp) VALUES ('Financial Contribution', '{moneyNotification}', '{timestamp}')".format(moneyNotification=currentMoneyNotification, timestamp=getTimestamp()))
# previous money notification
conn.execute(
    "INSERT INTO notifications (category, notification, timestamp) VALUES ('Financial Contribution', '{moneyNotification}', '{timestamp}')".format(moneyNotification=previousMoneyNotification, timestamp=getTimestamp(datetime.fromisoformat('2020-04-27'))))
# current vaccine notification #1
conn.execute("INSERT INTO notifications (category, notification, timestamp) VALUES ('Vaccination Distribution', "
             "'{vaccineNotification}', '{timestamp}')".format(vaccineNotification=currentFirstVaccineNotification,
                                                              timestamp=getTimestamp()))
# current vaccine notification #2
conn.execute("INSERT INTO notifications (category, notification, timestamp) VALUES ('Vaccination Distribution', "
             "'{vaccineNotification}', '{timestamp}')".format(vaccineNotification=currentSecondVaccineNotification,
                                                              timestamp=getTimestamp()))
# previous vaccination notification
conn.execute("INSERT INTO notifications (category, notification, timestamp) VALUES ('Vaccination Distribution', "
             "'First vaccine was distributed in America', '{timestamp}')".format(timestamp=getTimestamp(datetime.fromisoformat('2020-12-14'))))
conn.execute("INSERT INTO notifications (category, notification, timestamp) VALUES ('Vaccination Distribution', "
             "'Pfizer vaccine was approved by FDA', '{timestamp}')".format(timestamp=getTimestamp(datetime.fromisoformat('2020-09-03'))))
conn.execute("INSERT INTO notifications (category, notification, timestamp) VALUES ('Vaccination Distribution', "
             "'Moderna vaccine was approved by FDA', '{timestamp}')".format(timestamp=getTimestamp(datetime.fromisoformat('2020-07-26'))))
conn.execute("INSERT INTO notifications (category, notification, timestamp) VALUES ('Vaccination Distribution', "
             "'{vaccineNotification}', '{timestamp}')".format(vaccineNotification=previousFirstVaccineNotification,
                                                              timestamp=getTimestamp(datetime.fromisoformat('2021-02-06'))))
conn.execute("INSERT INTO notifications (category, notification, timestamp) VALUES ('Vaccination Distribution', "
             "'{vaccineNotification}', '{timestamp}')".format(vaccineNotification=previousSecondVaccineNotification,
                                                              timestamp=getTimestamp(datetime.fromisoformat('2021-02-06'))))

conn.commit()

print("Database notifications.db created")
