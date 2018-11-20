# Exercise 3.3
print("Exercise 3.3");
# create the lists
forward = [];
backward = [];
values = ["a", "b", "c"];

# populate forward and backward
for item in values:
    forward.append(item);
    backward.insert(0, item);
# print them
print(forward,backward);

# now reverse the order of one and check they are the same
forward.reverse();

if forward == backward:
    print("Lists are the same.");

# Exercise 3.4
print("Exercise 3.4");
# create the list
countries = ["uk", "usa", "uk", "uae"];

# display properties of list
dir(countries)

# display some docs
help(countries.count)

# count number of times uk appears in the list
print(countries.count("uk"));
