jedi('Anakin Skywalker').
jedi('Obi-wan Kenobi').
jedi('Yoda').
jedi('Luke Skywalker').
jedi('Qui-gon Jinn').

sith('Count Dooku').
sith('Darth Maul').
sith('Darth Vader').
sith('Emperor').
sith('Darth Plagueis').

rebels('Chewbacca').
rebels('Leia Organa').
rebels('Lando Calrissian').
rebels('Han Solo').
rebels('Sabine Wren ').

empire('Boba Fett').
empire('Bossk').
empire('Stormtrooper').
empire('Admiral Tarkin').
empire('Admiral Thrawn').

teacher('Obi-wan Kenobi','Anakin Skywalker').
teacher('Qui-gon Jinn', 'Obi-wan Kenobi').
teacher('Count Dooku', 'Qui-gon Jinn').
teacher('Yoda', 'Count Dooku').
teacher('Emperor', 'Count Dooku').
teacher('Emperor', 'Darth Maul').
teacher('Emperor', 'Darth Vader').
teacher('Darth Plagueis', 'Emperor').

killed('Darth Plagueis', 'Emperor').
killed('Darth Maul','Obi-wan Kenobi').
killed('Qui-gon Jinn', 'Darth Maul').
killed('Anakin Skywalker', 'Darth Vader').
killed('Bossk', 'Han Solo').
killed('Admiral Tarkin', 'Luke Skywalker').
killed('Count Dooku', 'Anakin Skywalker').

goodness(X) :- jedi(X); rebels(X).
evil(X) :- sith(X); empire(X).
grand_teacher(X, Z) :- teacher(X, Y), teacher(Y, Z).
enemies(X, Y) :- (evil(X), goodness(Y)) ; (goodness(X), evil(Y)).
force_wielder(X) :- jedi(X); sith(X).
soldier(X) :- empire(X); rebels(X).
irony(X, Y) :- teacher(X, Y), killed(X, Y).
