teacher('Obi-wan Kenobi','Anakin Skywalker').
teacher('Emperor', 'Darth Vader').
teacher('Emperor', 'Yoda').
killed('Count Dooku', 'Anakin Skywalker').
killed('Obi-wan Kenobi', 'Anakin Skywalker').

rebels('Luke Skywalker'); jedi('Luke Skywalker').
empire('Darth Vader'), not(jedi('Darth Vader')).
empire('Emperor'), sith('Emperor').
jedi('Ahsoka Tano'), not(soldier('Ahsoka Tano')).
sith('Darth Vader'); jedi('Darth Vader').

teacher('Emperor', X).
teacher(X, 'Anakin Skywalker').
teacher(X, 'Count Dooku').
killed('Darth Maul', Y).
killed(X, 'Darth Vader').

goodness('Obi-wan Kenobi').
grand_teacher('Emperor', X), killed(X, Y).
goodness(X), teacher(X, Y), evil(Y).
force_wielder('Ahsoka Tano').
irony(X, 'Emperor'), teacher(X, Y).
