# Description

Parses each file in a given directory and provide all matching signatures (magic numbers) to determine the file type.

# Usage

`main.py [-h] --path PATH [--headerBytes HEADERBYTES] [--trailerBytes TRAILERBYTES]`

| Option | Short | Type | Default | Description |
|---|---|---|---|---|
|--path | -p | String | - | Path of the directory  |
|--headerBytes | -e | Int | 512 | Number of first file bytes to read |
| --trailerBytes | -t | Int | 32 | Number of last file bytes to read |

# Example

`python main.py -p "path/to/directory" -e 128 -t 32 > example.txt`

Result:

```

################################################################################

Magic Number Checker by 5f0
Indicates the type of the file based on their magic number

Current working directory: /media/sf/software/magic-number-checker
Investigate files in: example/

Current Datetime: 01/01/1970 10:11:12

################################################################################

Investigated File: ./example.pdf

------------------------- File Hex - First 128 Bytes --------------------------
2550 4446 2d31 2e33 0a25 c4e5 f2e5 eba7 f3a0 d0c4 c60a 3420 3020 6f62 6a0a 
3c3c 202f 4c65 6e67 7468 2035 2030 2052 202f 4669 6c74 6572 29af 466c 6174 6544 
6563 6f64 6521 3e3e 0a73 7442 6561 6d0a 7801 b597 6f3f a24a 14c6 dffb 294e faaa 
4d90 f2d7 ea7d b514 b14e 16c1 8571 7b9b f40d e2a8 ec1a 7419 dca6 dffe 9e01 aa2e 
6d8c 

------------------------- File Hex - Last 32 Bytes --------------------------
6133 333e 205d 203e 3e0a 7374 6172 7478 7265 660a 3238 3142 300a 2525 454f 
460a 

--- Description ---> PDF file
-- Header Offet ---> 0
-------- Header ---> 2550 4446
------- Trailer ---> 2525 454f 46
----- Extension ---> PDF|FDF
---- File Class ---> Word processing suite

################################################################################
Execution Time: 0.005403 sec
################################################################################
```
You can find the  result [here](./example/example.txt).

# Credits

The file signatures are taken from [Gary Kessler](https://www.garykessler.net/library/file_sigs.html). The license for the signatures can be found [here](./data/GKA_software_license.pdf). You can download the originals [here](https://www.garykessler.net/software/index.html#filesigs). Thank you for your great work, Gary.

# License

MIT