# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!

def show_excitement():
    str=""
    i=0
    while(i<5):
        str=str+"I am super excited for this course! "
        i=i+1
    return str


print show_excitement()
