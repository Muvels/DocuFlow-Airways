def rm_non_printable(input_str: str):
     return ''.join(c for c in input_str if c.isprintable())

def rm_whitespaceprefixandsufix(input_str_arr: list[str]):
    output_str_arr = []
    for element in input_str_arr:
        output_str_arr.append(element.strip(" "))
    return output_str_arr

def isonlyonechar(input_str: str):
    if len(rm_non_printable(input_str).strip(" ")) == 1:
        return 1
    else:
        return -1

def performStringNormalisation(input_str: str):
    i = 0
    input_str_arr = input_str.split("\n")
    input_str_arr = rm_whitespaceprefixandsufix(input_str_arr)
    for string in input_str_arr:
        string = rm_non_printable(string)
        if isonlyonechar(string) == 1:
            del input_str_arr[i]
        else:
            input_str_arr[i] = string
        i = i+1
    return '\n'.join(input_str_arr)


