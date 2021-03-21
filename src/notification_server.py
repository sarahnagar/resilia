from bottle import Bottle, run, route

notificationApp = Bottle()  # let's create our own instance of the app


@notificationApp.route('/')
def root():
    """ Checks that the app is alive and healthy """
    return "Notification Server Is Up and Running!"


@notificationApp.route('/notification')
def getNotifications():
    """ Returns the notifications """
    return {"Notification1": "Welcome Sarah"}


run(notificationApp, host='localhost', port=8080, debug=True)

