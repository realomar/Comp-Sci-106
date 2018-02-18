function [accum] = simulateReactor(vector, time)
    % Estimates the accumulation value at a given time
    % Params: vector (a polynomial), time (seconds)
    % Returns: accum (value of current accumulation, an estimate)
    accum = polyval(vector,time);
end