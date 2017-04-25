% MM Project 1
% Prints out random question found in the text
% and then prints the generated answer to the word
% present in the question
% in - source text path
% out - output text path
%usage: questiongen("../data/butalci.txt", "../data/butalci/basic")
function questiongen(in, out)

questionWords = ["Kako";"Kdaj";"Zakaj";"Kam";"Kdo"];

randomQuestion = questionWords(randi(5),1:5);

textgen("../data/butalci/basic", "./question.out", 10, -1)
question = textread("./question.out", "%s");
delete("./question.out");
fid = fopen("../data/qa.txt", "w");
fputs(fid, "Vprasanje: ");
fputs(fid, randomQuestion);
longestWord = question{1};
for i = 1:rows(question)
	if(length(longestWord) <= length(question{i}))
		longestWord = question{i};
	endif
	fputs(fid, question{i});
	if(i < rows(question))
		fputs(fid, " ");
	endif
endfor
fputs(fid, "?");
fclose(fid);

% need random text based on word randomWord

textgen("../data/butalci/basic", "./answer.out", randi(5)+10, -1, longestWord);
answer = textread("./answer.out", "%s");
delete("./answer.out");
fid = fopen("../data/qa.txt", "a");
fputs(fid, "\nOdgovor: ");
for i = 1:rows(answer)
	if(i == 1)
		answer{i}(1) = toupper(answer{i}(1));
	endif
	fputs(fid, answer{i});
	if(i < rows(answer))
		fputs(fid, " ");
	endif
endfor
fputs(fid, ".\n");
fclose(fid);
