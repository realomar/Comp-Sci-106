function [coeff,pRawData,pOrder2,pBestOrder] = graphFit(vector)
    % Finds and graphs the optimal curveFit for a given data
    % Param: vector (data, measured every 10s)
    % Output: coeff, a polynomial representing the data with degree between 2 and 8
    % and pRawData a plot of raw data, pOrder2, plot of order 2, pBestOrder, plot of ideal polyfit.
    poly = curveFit(vector,2);
    time = 0:10:(length(vector)*10-1);
    approx = polyval(poly,time);
    diff = approx - vector;
    avg = mean(diff);
    stdev = std(diff);
    pOrder2 = get(plot(time,approx,'+'));
    
    for (i = 3:8)
        newPoly = curveFit(vector, i);
        newApprox = polyval(newPoly,time);
        newDiff = newApprox - vector;
        newAvg = mean(newDiff);
        newStdev = std(newDiff);
        if (newAvg > avg)
            break;
        elseif ((newAvg < 0.01) && (newStdev < 0.01))
            poly = newPoly;
            break;
        else
            poly = newPoly;
            diff = newDiff;
            avg = newAvg;
            stdev = newStdev;
        end
    end
    pRawData = get(plot(time,vector,'o'));
    pBestOrder = get(plot(time,polyval(poly,time),'x'));
    coeff = poly;
    xlabel('seconds')
    ylabel('accumulation of chemical')
    legend('Raw data: o', '2nd order: +', 'Ideal order: x')
end