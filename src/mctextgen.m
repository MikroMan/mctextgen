% MM Project 1
% Generate text using Markov chains
% in - Path to source text
% out - Path to destination file
% length - how much words to generate
% seed - seed for random generator, if < 0 do not seed

function mctextgen(in, out, len, seed=3);
    
    printf("Reading data from %s:",in);
    % Save RNG state
    
    % Seed the rng
    if(seed > 0)
        rng_state = rand("state");
        rand("seed", seed);
    endif
    text = textread(in, "%s"); %read text to cell array


    % Find unique words in text - sorted by ascending alphabetical order
    words = unique(text);

    printf(" %d words in file, %d unique words.\n",rows(text), rows(words));

    P = build_matrix(words, text);

    printf("Done.\n");


    % Randomly generate an initial state
    x0 = randi(rows(words));

    printf("Initial state %d, generating %d next states... ", x0, len);

    % Use a generator to get a vector of states
    states = state_gen(P, x0, len);
    printf("Done.\n");
    
    to_file(out,words,states);

    % Restore RNG state
    if(seed > 0)
         rand("state", rng_state);
    endif
endfunction


function to_file(out, words, states);
    printf("Writing to file %s... ", out);
    fid = fopen(out, "w"); % Open file descriptor

    for i = 1:columns(states)
        
        % Write string to output file
        fputs(fid, words{states(1,i),1});
        fputs(fid, " ");
        if(mod(i, 10) == 0)
            fputs(fid, "\n");
        endif          
    endfor

    printf("Done.\n");

    % Close file
    fclose(fid);
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