##
## EPITECH PROJECT, 2018
## Makefile
## File description:
## Makefile for python projects
##

MAKE	=	make

PYCACHE	=	__pycache__/

RM		=	rm -f

NAME	=	pbrain-gomoku-ai.py

all	:
	cp __main__.py $(NAME)

tests_run :
	python3 -m unittest discover

fclean	:	clean
	$(RM) $(NAME)

clean	:
	find ./ -name "__pycache__" -type d -exec rm -rv {} +

re	:	fclean all

.PHONY	: all fclean clean re tests_run
