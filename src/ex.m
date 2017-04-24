% Generates 10 +1 words of text to simple.out file.
% Static seed 3 is used - every output is the same
mctextgen("../data/ex1.txt", "./simple.out", 10);

% Generates 10 + 1 words of text
% User defined seed for repeatability
mctextgen("../data/ex1.txt", "./seeded.out", 10, 42);


% Seed -1 disables RNG seeding, causes randomised results
mctextgen("../data/ex1.txt", "./unseeded.out", 10, -1); 
