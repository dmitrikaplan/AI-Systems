% джедаи
jedi('Anakin Skywalker').
jedi('Obi-wan Kenobi').
jedi('Yoda').
jedi('Luke Skywalker').
jedi('Qui-gon Jinn').

%ситхи
sith('Count Dooku').
sith('Darth Maul').
sith('Darth Vader').
sith('Emperor').
sith('Darth Plagueis').

%повстанцы
rebels('Chewbacca').
rebels('Leia Organa').
rebels('Lando Calrissian').
rebels('Han Solo').
rebels('Sabine Wren ').

%имперцы
empire('Boba Fett').
empire('Bossk').
empire('Stormtrooper').
empire('Admiral Tarkin').
empire('Admiral Thrawn').

%предикат вида teacher(X, Y), означающий, что X является учителем Y
teacher('Obi-wan Kenobi','Anakin Skywalker').
teacher('Qui-gon Jinn', 'Obi-wan Kenobi').
teacher('Count Dooku', 'Qui-gon Jinn').
teacher('Yoda', 'Count Dooku').
teacher('Emperor', 'Count Dooku').
teacher('Emperor', 'Darth Maul').
teacher('Emperor', 'Darth Vader').
teacher('Darth Plagueis', 'Emperor').

%предикат вида killed(X, Y), означающий, что X был убит Yом
killed('Darth Plagueis', 'Emperor').
killed('Darth Maul','Obi-wan Kenobi').
killed('Qui-gon Jinn', 'Darth Maul').
killed('Anakin Skywalker', 'Darth Vader').
killed('Bossk', 'Han Solo').
killed('Admiral Tarkin', 'Luke Skywalker').
killed('Count Dooku', 'Anakin Skywalker').

% правило, которое проверяет воюет ли X за сторону добра
goodness(X) :- jedi(X); rebels(X).
% правило, которое проверяет воюет ли X за сторону зла
evil(X) :- sith(X); empire(X).
% правило, которое проверяет является ли X учителем учителя Z
grand_teacher(X, Z) :- teacher(X, Y), teacher(Y, Z).
% правило, которое проверяет являются ли X и Y врагами
enemies(X, Y) :- (evil(X), goodness(Y)) ; (goodness(X), evil(Y)).
%правило, которое проверяет владеет ли силой X
force_wielder(X) :- jedi(X); sith(X).
%правило, которое проверяет является ли X солдатом
soldier(X) :- empire(X); rebels(X).
%правило, которое проверяет является ли иронией связь X и Y
irony(X, Y) :- teacher(X, Y), killed(X, Y).
