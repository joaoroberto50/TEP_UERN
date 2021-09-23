# Makefile para biblioteca Util
# JOAO ROBERTO - TEP - UERN

CC = gcc
INCLUDE = ./lib_U/
LINKER = util
LINK = ./lib_U/
SRC = main.c
OBJ = $(SRC:.c=.o)


all:
	$(CC) -I $(INCLUDE) -l $(LINKER) -L $(LINK) -o $(OBJ) $(SRC)

run:
	LD_LIBRARY_PATH=$(INCLUDE) ./$(OBJ)

clean:
	rm ./$(OBJ)
