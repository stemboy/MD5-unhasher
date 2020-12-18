# md5-unhasher
This program will decrypt md5 hashes using a database that you can help mine, when this app is out of development, you can help the global cause of ruining the point of md5 hashes.

# Usage 
```
md5-unhasher.py [Option]  
                --help               - Show this page  
                --gui-only           - Run only the gui  
                --array-create-only  - Run the array creator only
```

# How it works
The [code](msic/array_creator.py) creates and array of strings and md5-hashes. The strings are made up of 91 characters that are lower and upper case, numbers and special characters. Then it encrypts them in md5 and saves them to an array with the md5 as the key and string as the value, this means that you can use a md5 hash to get the string that you didn't know before.