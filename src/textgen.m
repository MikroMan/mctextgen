% MM Project 1
% Generate text using Markov chains
% in - path to source folder
% out - Path to destination file
% length - how much words to generate
% seed - seed for random generator, if < 0 do not seed

%usage: textgen("../data/butalci/basic", "./sample.out", 100, -1 );



function textgen(in, out, len, seed=3, x0=0);
    
    printf("Reading data from %s:",in);
    % Save RNG state
    
    % Seed the rng
    if(seed > 0)
        rng_state = rand("state");
        rand("seed", seed);
    endif
    
    tic();
    P = csvread([in "/matrixdump"]);
    words = textread([in "/uniques"], "%s");
    toc();

    if(x0 == 0)
        % Randomly generate an initial state
        x0 = randi(rows(words));
    else
        for b = 1:rows(words)
            if(strcmp(x0,words{b}) == 1)
                x0 = b;
            endif
        endfor
    endif

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
