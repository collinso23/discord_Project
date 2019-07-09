#!/bin/bash

myFunction()
{
    python3 DnD_DB_Scrapper.py $section $specifier $otherSpecifier
}

read -p "spell, item, monster, race, or class followed by search" section specifier otherSpecifier

myFunction $section $specfifier $otherSpecifier
