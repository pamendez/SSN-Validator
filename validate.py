from errors import messages

def main():
    """
        Serves as the main entry point of the application.
    """

    ssn = input("Enter the social security number (SSN) with each part separated by a hyphen (-): ").strip()
    error_list = validate_ssn(ssn)
    if (len(error_list) == 0):
        print("\nThe SSN is valid.")
        pass

    else:
        print("\nThe SSN is invalid. The following error(s) were found:")
        for error_code in error_list:
            key, subkey = error_code
            print(f"- {messages.get(key).get(subkey)}")
        pass


def validate_ssn(input_ssn):
    """
        Checks the validity of any social security number entered.
        * If the social security number satisfies every condition, then it is valid.
        * Otherwise, the social security number is invalid.
    """

    error_list = []
    input_ssn_parts = input_ssn.split("-")
    ssn_parts_len = [3, 2, 4]
    index = 0

    if (len(input_ssn_parts) == 3):
        collection = zip(input_ssn_parts, ssn_parts_len)
        for item in collection:
            index += 1
            if (len(item[0]) == item[1]):
                if not (item[0].isdigit()):
                    error_list.append((2, index)) # Status code for presence of letters in any of the parts.
                    pass

                else:
                    part_as_number = int(item[0])
                    if (part_as_number == 0) or (index == 1 and (part_as_number == 666 or part_as_number > 899)):
                        error_list.append((1, index)) # Status code for invalid number in current part.
                        pass

                    else:
                        continue
                pass

            else:
                error_list.append((3, index)) # Status code for lack of digits in any of the parts.
                pass
        pass

    else:
        if (len(input_ssn_parts) > 3):
            error_list.append((4, 1)) # Status code for excess of parts.
            pass

        else:
            error_list.append((4, 2)) # Status code for insufficient of parts.
            pass
        pass

    return error_list

if __name__ == "__main__":
    main()
    pass