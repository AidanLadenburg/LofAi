

# LofAi
#### This is the project page for LofAi, an extension of [Musika!](https://github.com/marcoppasini/musika) and the culmination of 3 months of work (Oct 2022 - Jan 2023). The goal of This project was to create believable-sounding Lofi music, in faster-than-real-time. 
#### All results presented here were generated in the above time period and represent (to the best of my knowledge) near-SOTA results for the time, under the given constraints.

#### For privacy reasons, I've opted to keep the model private for now, so this page exists to host some of the data filtering tools used in the project as well as showcase the results.

### Files
* remp3.py
	* convert batch files to mp3 with ffmpeg
* transcribe.py
	* data processing tool to identify music files with vocals using adjustable threshold 
* Current Samples
	* file containing a small number of raw sample model outputs
###  Parameters
* Encoding
	* max_lat_len: 1024
	* lat_depth: 128
* Training
	*  base_channels: 384/512
	* lr:  0.00004
	* 1.4M steps
#### See [Musika!](https://github.com/marcoppasini/musika) for more details


### Sample visualization (Early model, Nov 2022)
https://github.com/AidanLadenburg/LofAi/assets/43151719/d676c100-9287-46e1-98f5-7ca14fd32589



## The final video project can be found [here](https://www.youtube.com/watch?v=YpGc9_Q3QeE). Please check it out and feel free to message me with any questions!
#### aidanladenburg@gmai.com
