from tracker import Tracker
import csv
from rich.console import Console
from logger import *
console = Console()


def menu():
    logger = logging()
    console.print("Select an option")
    print("")
    print("")
    console.print("1. Start trackers")
    console.print("2. exit")
    option = input(">")
    match option:
        case '1':
            logger.success("Tracker starting")
            while True:
                with open('wallets.csv','r') as csvFile:
                    read_file = csv.DictReader(csvFile)
                    
                    for row in read_file:
                    
                    
                            Tracker(name =row['name'],address =row['address'],api_key = "ENTER API KEY").fetch_transactions()
                
                
            

        case "2":
            print("Exiting")
            
            exit()

if __name__ == "__main__":
    menu = menu()