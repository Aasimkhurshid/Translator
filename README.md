
# Langugage Translator for SRT files
The project is for language translation.
It has two modes:
1. Interactive Language translation    
2. Non-interactive.

# (Usage - Command line: )
1. Install requirements.txt using pip install -r requirements.txt
2. Run python main.py

# Usage 02 - Interactive IDE
1. For this, uncomment the main() and comment the rest.  
2. It will request the type of translation you want, From files or simple text translation;
3. Then it will make requests for source language, target language and text or files addresses (also a directory in which you want to save results).
4. NOTE: While giving path as input, just provide the path without any quotation (/path/to/directory/).
,
# Usage 03 (Docker)
This requires that you have docker in your system.  
1. Create a file named docker in the directory of the project using:  touch docker
2. Add instructions in docker file. (Docker file with instrucitons is added in the directory)
3. Build docker file to create image using:  
  docker build -t translator . (dot in the end is required)
4. Run the image to create and run container using:
docker run translator

Copyright: we use pre-trained model of deep-translator which is open-source under the MIT License.


