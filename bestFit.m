function [poly] = bestFit(vector)
    % Finds the optimal curveFit for a given data
    % Param: vector (data, measured every 10s)
    % Output: a polynomial representing the data with degree between 2 and 8
    isComplete = 0;
    n = 2;
    L = 10 * length(vector);
    testVals = [];
    avg = [9999];
    while(isComplete == 0)
        testPoly = curveFit(vector, n);
        for(i = 0:10:(L-1))
            testVals = [testVals, polyval(testPoly,i)];
        end
        diff = testVals - vector;
        avg = [avg,abs(mean(diff))];
        stdev = std(diff);
        if(avg(n) > avg(n-1))
            poly = curveFit(vector,n-1);
            isComplete = 1;
        elseif(avg(n) < .01 && stdev < .01)
            poly = curveFit(vector,n);
            isComplete = 1;
        elseif(n == 8)
            poly = curveFit(vector,n);
            isComplete = 1;
        else
            n = n+1
        end
    end
end