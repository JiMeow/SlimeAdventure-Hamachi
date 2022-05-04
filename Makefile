# server and client makefiles for MinZung project
sm:
	python FPSmin\server.py
cm:
	python FPSmin\client.py


#client makefiles for JiMeow project
c:
	python JiMeow\client.py

# How to use
# use makefile to run server and client 
# run server and client in separate terminal

# example for normal make
# T1: make sm
# T2: make cm

# example for mingw32-make
# T1: mingw32-make sm
# T2: mingw32-make cm
