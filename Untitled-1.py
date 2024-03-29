while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # 5. Check the customer's input
        match keep_ordering:
            case "Y":
                    print('is this the right order')
        #    case "N":
        #       print('Your order is complete')
                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order
            case "N":
                # Since the customer decided to stop ordering, thank them for
                # their order
        #       place_order = False
        #       keep_ordering = False
                print('Your order is complete')
                break
                # Exit the keep ordering question loop

