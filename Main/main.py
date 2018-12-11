import json
import zlib
import sys
import random
array = []
for x in range(0, 360):
    array.append(random.randrange(0, 1000))

jsonform = json.dumps(array)
raw_form = jsonform.encode("ascii")
print(sys.getsizeof(raw_form))
compressed_form = zlib.compress(raw_form)
print(sys.getsizeof(compressed_form))
uncompressed = zlib.decompress(compressed_form)
new_json = json.loads(uncompressed.decode("ascii"))
