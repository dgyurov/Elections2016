import config
import os
from gathering import fbsdk


def main():

    # The main method of the program
    print 'Program started!'
    gathering()


def gathering():

    # Clean up the Data directory before the new data generation if enabled
    if config.clearDataFolder:
        filelist = [f for f in os.listdir("./data")]
        for f in filelist:
            os.remove('./data/'+f)

    # Generate data files using the FB Graph API
    fbsdk.main()


def analysis():
    # TODO analysis
    print 'The analysis part of the program is coming soon'


def visualisation():
    # TODO visualisation
    print 'The visualisation part of the program is coming soon'

if __name__ == '__main__':
    # main.py executed as script
    main()
