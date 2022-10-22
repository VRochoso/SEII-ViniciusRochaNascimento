SRC = ./src
INCLUDE = ./include
BIN = ./bin
OBJ = ./obj
APPS = ./apps

all: libed myapps

libed: \
	float_vector.o \
	mytime.o

myapps:
	gcc $(APPS)/app.c $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/app
	gcc $(APPS)/app_com_my_tyme.c $(OBJ)/*.o -I $(INCLUDE) -o $(BIN)/app_com_my_tyme

%.o: $(SRC)/%.c $(INCLUDE)/%.h
	gcc -c $< -I $(INCLUDE) -o $(OBJ)/$@

run:
	./bin/app

clean:
	rm -rf ./bin/* ./obj/*
