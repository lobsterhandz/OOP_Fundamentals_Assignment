class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0  # Initialize participant count to 0

    def add_participant(self):
        self.participant_count += 1
        print(f"Added a participant. Total participants: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count

# Demonstration
def main():
    # Create an Event object
    event = Event("Python Conference", "2023-07-25")
    
    # Add participants
    event.add_participant()
    event.add_participant()
    
    # Get current participant count
    count = event.get_participant_count()
    print(f"Current participant count for {event.name}: {count}")

if __name__ == "__main__":
    main()
