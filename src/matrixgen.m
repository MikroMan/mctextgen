% MM Project 1
% Generate simple P matrix for Markov chain generator  
% Dumps P matrix and word vector to CSV for textgen reader
% in - Path to source text
% out - Path to folder for output files (ex. "./abc", ".")

%usage: textgen("../data/butalci.txt", "../data/butalci/basic");


function matrixgen(in, out);
    
    printf("Reading data from %s:",in);

    text = textread(in, "%s"); %read text to cell array


    % Find unique words in text - sorted by ascending alphabetical order
    words = unique(text);

    printf(" %d words in file, %d unique words.\n",rows(text), rows(words));
    tic();
    P = build_matrix(words, text);
    toc();
    printf("Done.\n");

    csvwrite([out "/matrixdump"], P);

    fid = fopen([out "/uniques"], "w");
    for i = 1:rows(words)
       fputs(fid, words{i});
       fputs(fid, "\n");
    endfor

endfunction


function P = build_matrix(words, text);

 % Allocate matrix
    P = zeros(rows(words), rows(words));
    
    printf("Generating P matrix... ");
    %For every word in file...
    for i = 2:rows(text)
        % idx1 = initial state, idx2 = next state
        idx1 = find(ismember(words,text(i-1,1)));
        idx2 = find(ismember(words,text(i,1)));

        % Increment count for this pair of states
        P(idx1,idx2) += 1;
    endfor

        % Normalise sums to make matrix P stohastic
    for i = 1:rows(P)
        s = sum(P(i,:));
        if(s > 0) % check for 0 to avoid zero division - NaN
             %Divide every cell in row with sum of row
             P(i,:) = P(i,:)/sum(P(i,:));
        endif
       endfor

endfunction