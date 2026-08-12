
from check_computers import check_computers
from count_available import count_available
from display_status import display_status


while True:
    # Check the computers
    computers = check_computers()

    # Count available computers
    available = count_available(computers)

    # Display the lab status
    display_status(computers, available)

    # Ask whether to continue monitoring
    choice = input(
        "\nPerform another monitoring cycle? (Y/N): "
    ).upper()

    if choice == "N":
        print("\nMonitoring stopped.")
        break