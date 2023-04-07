def numbers_of_letters(n):
    dict = {"1": "one", "2": "two",
            "3": "three", "4": "four",
            "5": "five", "6": "six",
            "7": "seven", "8": "eight",
            "9": "nine", "0": "zero"}
    result = []
    str1_for_res = ""
    str2_for_res = ""
    str3_for_res = ""
    str4_for_res = ""
    for i in str(n):
        str1_for_res += dict.get(i)
    result.append(str1_for_res)
    str2_for_res += dict.get(str(len(str1_for_res)))

    result.append(str2_for_res)
    str3_for_res += dict.get(str(len(str2_for_res)))

    result.append(str3_for_res)
    str4_for_res += dict.get(str(len(str3_for_res)))

    result.append(str4_for_res)
    return result


print(numbers_of_letters())
