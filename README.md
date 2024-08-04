# asiair_file_sorter

This script will take a raw dump of files generated with ASIAir and sort them into a useable directory

This will generate the following directory structure
```
{astro_project_folder}
|--Lights
  |--H
  |--S
  |--O
  |--{any applicable filter found in your Lights files}
|--Flats
  |--{date}
    |--H
    |--S
    |--O
    |--{any applicable filter found in your Flats files}
|--PI (pixinsight directory to output batch processing etc)
|--raw_dump (this is where you should dump all your raw files from ASIAir)
|--bad_subs 
|--subframes
  |--S
  |--H
  |--...
```


Steps:
1. Create a directory with your project name
2. Create a subfolder in the directory above called 'raw_dump'
3. update HOME_DIRECTORY in config.py with the path to your astro folder that contains your projects e.g. '/home/mike/astrophotography'
4. dump all ASIAir Flats and Light files into the raw_dump directory
    - this script assumes you have already made master darks and bias files so it will not handle those
5. run this script
