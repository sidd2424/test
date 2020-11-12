lt = ["s", "i", "d", "d", "h","a", "r", "t", "h"]
lt = list(dict.fromkeys(lt))
print(lt)


def convert(list): 
    return tuple(list)

 
print(convert(lt))
print(min(lt))
print(max(lt))
