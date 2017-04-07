% MM Project 1
% Generate a vector of states
% P - Markov chain matrix
% x0 - initial state
% tmax - maximum amount of steps
function states = state_gen(P, x0, tmax);

n = length(P); %save matrix length

%initialise state vector
states = [x0, zeros(1, tmax)];

% save cumulative sum for easier usage of find
P = cumsum(P')';

%pozenemo simulacijo
for k = 2:(tmax+1)
	states(1, k) = find(P(states(1, k-1), :) >= rand(), 1);
end