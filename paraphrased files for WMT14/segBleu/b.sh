
for file in /home/shreyaa/aditya/files/*
do
    counter = $(($counter + 1))
    morfessor-segment -l adi $file > "/home/shreyaa/aditya/output/"$counter".txt"
done 