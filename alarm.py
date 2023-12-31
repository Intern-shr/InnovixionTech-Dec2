import datetime
import time
import winsound  # This module is for Windows system. For other systems, you may need to use a different module.

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            # Play a sound (you can replace this with your preferred method of alert)
            winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
            break
        time.sleep(1)

def main():
    print("Welcome to the Alarm Clock App!")
    
    while True:
        try:
            # Get user input for the alarm time
            alarm_time_str = input("Set the alarm time (HH:MM:SS): ")
            alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M:%S").strftime("%H:%M:%S")
            
            # Set the alarm
            set_alarm(alarm_time)
            
            # Ask the user if they want to set another alarm
            another_alarm = input("Do you want to set another alarm? (yes/no): ").lower()
            if another_alarm != 'yes':
                print("Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter the time in the format HH:MM:SS.")

if __name__ == "__main__":
    main()
