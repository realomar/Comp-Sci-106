% Omar Ahmad / Ryan Fisher

function [sig] = binarySignal(signal, threshold)
    % Converts an analog input to a binary signal
    % Parameters: input analog signal, and threshold that separates a binary 1 from a 0
    % Returns: binary version of that signal
    signal = abs(signal);
    windowSize = 20;
    b = (1/windowSize)*ones(1,windowSize);
    a = 1;
    signal = filter(b,a,signal);
    signal = signal > threshold;
    sig = signal;
end

function [token] = tokenizeSignal(binary_signal)
    % Converts the newly binary signal to a sequence of 1s and 0s
    % Parameters: input binary signal
    % Returns: "token," a sequence of 1s and 0s
    i = 1;
    A = ones(size(binary_signal),2);
    for(pos = 1:size(binary_signal))
        if(pos > 1)
            if(binary_signal(pos) == binary_signal(pos-1))
                A(i,1) = A(i,1) + 1;
            else
                i = i + 1;
            end
        end
        if(binary_signal(pos) == 0)
            A(i,2) = 0;
        else
            A(i,2) = 1;
        end
    end
    token = A(1:i,1:2);
end

function [message] = tokensToMessage(tokens, unittime)
    % Converts the tokens into a message
    % Parameters: tokens [binary sequence], unittime
    % Returns: a string message
    message = '';
    symbol = '';
    for i = 1:rows(tokens)
        if(tokens(i,1) > 2*unittime && tokens(i,2) == 0)
            message = [message,getSymbol(symbol)];
            if(tokens(i,1) > 4*unittime)
                message = [message,' '];
            end
            symbol = '';
        elseif(tokens(i,1) > 2*unittime && tokens(i,2) == 1)
            symbol = [symbol,'-'];
        elseif(tokens(i) > unittime/2 && tokens(i,2) == 1)
            symbol = [symbol,'.'];
        else

        end
    end
    message = [message, getSymbol(symbol)];
end
