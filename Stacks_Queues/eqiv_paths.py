def get_equiv(path):
    folders=path.split("/")
    pathstack=[]
    is_absolute=path.startswith("/")
    for folder in folders:
        if folder in [".",""]:
            continue
        if folder=="..":
            try:
                pathstack.pop()
            except IndexError:
                if is_absolute:
                    raise ValueError("Invalid path name!")
        else:
            pathstack.append(folder)
    return "/".join(folder for folder in pathstack)



print(get_equiv("/.."))