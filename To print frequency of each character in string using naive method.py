test_str = "mississippi"

all_freq = {}

for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1

print ("Count of all characters in mississippi is :\n "
						    			+ str(all_freq))