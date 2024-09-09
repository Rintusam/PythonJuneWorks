

# *args (arguments tuple)
# **kwargs( keyword arguments dictionary)


def get_person(**kwargs):

    print(kwargs.get("name"))
    print(kwargs.get("work_place"))
    print(kwargs.get("native_place"))



get_person(name="rintu",work_place="kochi",native_place="palakkad")