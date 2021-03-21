import sqlite3
import json
import logging
from bottle import Bottle, run

notificationApp = Bottle()  # let's create our own instance of the app


@notificationApp.route('/')
def root():
    """ Checks that the app is alive and healthy """
    return "Notification Server Is Up and Running!"


@notificationApp.route('/notifications')
def getNotifications():
    """ Returns the notifications from the database"""
    # gets the data from the notifications db
    conn = sqlite3.connect('notifications.db')
    c = conn.cursor()

    # get all the data from the db except id (ie. timestamp, message, category)
    c.execute("SELECT category, timestamp, notification FROM notifications")
    result = c.fetchall()
    logging.debug("The database returned {} rows".format((len(result))))
    c.close()

    # format the data so the front end can consume it easily
    # we know the order of the data because it's the same order we passed into the select statement
    resultDict = [{'category': notification[0], 'timestamp': notification[1], 'notification': notification[2]} for notification in result]
    return json.dumps(resultDict)


run(notificationApp, host='localhost', port=8080, debug=True)




