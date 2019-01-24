% Analysis of average delay per hops
% Morning set
clear all
close all
clc

AMfile = xlsread('asiaworksmorning.xlsx', 'E:I');
%AMfile = xlsread('facebook afternoon.xlsx', 'E:I');
%AMfile = xlsread('facebook morning.xlsx', 'E:I');
hopsAM = zeros(length(AMfile), 1);
avgAM = zeros(length(AMfile), 1);
[row, column] = size(AMfile);

for i = 1:row
    if(AMfile(i,1) == 1)
        listIDAM(i) = i; 
        newlistIDAM = listIDAM(listIDAM ~= 0); 
    end

    hopsAM(i) = AMfile(i, 1);
    for j = 1:column
        if isnan(AMfile(i, j))
            AMfile(i, j) = 0.5;
        end
        avgAM(i) = sum(AMfile(i, 2:4))/3;
    end
end

for k = 1:length(newlistIDAM)
    if(newlistIDAM(k) == newlistIDAM(end))
        lastavgAM = AMfile(newlistIDAM(k): end, 5);
        lasthopsAM = AMfile(newlistIDAM(k): end, 1);
    else
        totavgAM{k} = AMfile(newlistIDAM(k):newlistIDAM(k+1)-1, 5);
        tothopAM{k} = AMfile(newlistIDAM(k):newlistIDAM(k+1)-1, 1);
    end
end

mondayAvgAM = totavgAM{1,1};
lmondayAvgAM = mondayAvgAM(length(mondayAvgAM));
mondayHopAM = tothopAM{1,1};
tuesdayAvgAM = totavgAM{1,2};
ltuesdayAvgAM = tuesdayAvgAM(length(tuesdayAvgAM));
tuesdayHopAM = tothopAM{1,2};
wednesdayAvgAM = totavgAM{1,3};
lwednesdayAvgAM = wednesdayAvgAM(length(wednesdayAvgAM));
wednesdayHopAM = tothopAM{1,3};
thursdayAvgAM = totavgAM{1,4};
lthursdayAvgAM = thursdayAvgAM(length(thursdayAvgAM));
thursdayHopAM = tothopAM{1,4};
fridayAvgAM = lastavgAM(length(lastavgAM));
fridayHopAM = lasthopsAM;

%%  Afternoon set
% clear all
% close all
% clc

AFfile = xlsread('asiaworksafternoon.xlsx', 'E:I');
%AFfile = xlsread('facebookafternoon.xlsx', 'E:I');
hopsAF = zeros(length(AFfile), 1);
avgAF = zeros(length(AFfile), 1);
[row, column] = size(AFfile);

for i = 1:row
    if(AFfile(i,1) == 1)
        listIDAF(i) = i; 
        newlistIDAF = listIDAF(listIDAF ~= 0); 
    end

    hopsAF(i) = AFfile(i, 1);
    for j = 1:column
        if isnan(AFfile(i, j))
            AFfile(i, j) = 0.5;
        end
        avgAF(i) = sum(AFfile(i, 2:4))/3;
    end
end

for k = 1:length(newlistIDAF)
    if(newlistIDAF(k) == newlistIDAF(end))
        lastavgAF = AFfile(newlistIDAF(k): end, 5);
        lasthopsAF = AFfile(newlistIDAF(k): end, 1);
    else
        totavgAF{k} = AFfile(newlistIDAF(k):newlistIDAF(k+1)-1, 5);
        tothopAF{k} = AFfile(newlistIDAF(k):newlistIDAF(k+1)-1, 1);
    end
end

mondayAvgAF = totavgAF{1,1};
lmondayAvgAF = mondayAvgAF(length(mondayAvgAF));
mondayHopAF = tothopAF{1,1};
tuesdayAvgAF = totavgAF{1,2};
ltuesdayAvgAF = tuesdayAvgAF(length(tuesdayAvgAF));
tuesdayHopAF = tothopAF{1,2};
wednesdayAvgAF = totavgAF{1,3};
lwednesdayAvgAF = wednesdayAvgAF(length(wednesdayAvgAF));
wednesdayHopAF = tothopAF{1,3};
thursdayAvgAF = totavgAF{1,4};
lthursdayAvgAF = thursdayAvgAF(length(thursdayAvgAF));
thursdayHopAF = tothopAF{1,4};
fridayAvgAF = lastavgAF(length(lastavgAF));
fridayHopAF = lasthopsAF;

%% Night set
%clear all 
%clc
PMfile = xlsread('asiaworksnight.xlsx', 'E:I');
%PMfile = xlsread('facebook night.xlsx', 'E:I');
%PMfile = xlsread('google afternoon.xlsx', 'E56:H72');
%PMfile = xlsread('facebooknight.xlsx', 'E:I');

hopsPM = zeros(length(PMfile), 1);
avgPM = zeros(length(PMfile), 1);
[row, column] = size(PMfile);

for i = 1:row
    if(PMfile(i,1) == 1)
        listIDPM(i) = i; 
        newlistIDPM = listIDPM(listIDPM ~= 0); 
    end

    hopsPM(i) = PMfile(i, 1);
    for j = 1:column
        if isnan(PMfile(i, j))
            PMfile(i, j) = 0.5;
        end
        avgPM(i) = sum(PMfile(i, 2:4))/3;
    end
end

for k = 1:length(newlistIDPM)
    if(newlistIDPM(k) == newlistIDPM(end))
        lastavgPM = PMfile(newlistIDPM(k): end, 5);
        lasthopsPM = PMfile(newlistIDPM(k): end, 1);
    else
        totavgPM{k} = PMfile(newlistIDPM(k):newlistIDPM(k+1)-1, 5);
        tothopPM{k} = PMfile(newlistIDPM(k):newlistIDPM(k+1)-1, 1);
    end
end

mondayAvgPM = totavgPM{1,1};
lmondayAvgPM = mondayAvgPM(length(mondayAvgPM));
mondayHopPM = tothopPM{1,1};
tuesdayAvgPM = totavgPM{1,2};
ltuesdayAvgPM = tuesdayAvgPM(length(tuesdayAvgPM));
tuesdayHopPM = tothopPM{1,2};
wednesdayAvgPM = totavgPM{1,3};
lwednesdayAvgPM = wednesdayAvgPM(length(wednesdayAvgPM));
wednesdayHopPM = tothopPM{1,3};
thursdayAvgPM = totavgPM{1,4};
lthursdayAvgPM = thursdayAvgPM(length(thursdayAvgPM));
thursdayHopPM = tothopPM{1,4};
fridayAvgPM = lastavgPM(length(lastavgPM));
fridayHopPM = lasthopsPM;

npathPM = i;
% pathChange = [npathAMm, npathAFm, npathPMm; npathAMt, npathAFt, npathPMt;...
%               npathAMw, npathAFw, npathPMw; npathAMth, npathAFth, npathPMth;...
%               npathAMf, npathAFf, npathPMf];
% bar(pathChange)
% set(gca,'xticklabel',{'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'});
% legend({'AM' 'AF' 'PM'})
%% Results
%plot(hopsAF, avgAF, 'o', hopsAF, avgPM, '*');
%plot(hopsAF, avgAF, 'k', 'LineWidth',2)
%loglog(hopsAF, avgAF, '-*')
%hold on
%plot(hopsPM, avgPM, 'LineWidth', 2)
%loglog(hopsPM, avgPM, '->')
%legend('Afternoon', 'Night')

figure(1)
avgdelayPlot = [lmondayAvgAM ltuesdayAvgAM lwednesdayAvgAM lthursdayAvgAM fridayAvgAM;...
                lmondayAvgAF ltuesdayAvgAF lwednesdayAvgAF lthursdayAvgAF fridayAvgAF;...
                lmondayAvgPM ltuesdayAvgPM lwednesdayAvgPM lthursdayAvgPM fridayAvgPM];
bar(avgdelayPlot)  
title('Average Delay End-End', 'FontSize', 20)
ylabel('Delay (ms)', 'FontSize', 18)
ylim([0 220])
set(gca,'xticklabel',{'Morning', 'Afternoon', 'Night'});
legend({'Mon' 'Tue' ' Wed' 'Thu' 'Fri'})


figure(2)
% plot(mondayHopPM, mondayAvgPM, '-*', 'LineWidth', 2)
% hold on
% plot(tuesdayHopPM, tuesdayAvgPM, '-o', 'LineWidth', 2)
% plot(wednesdayHopPM, wednesdayAvgPM, '->', 'LineWidth', 2)
% plot(thursdayHopPM, thursdayAvgPM, 'k', 'LineWidth', 2)
plot(fridayHopPM, lastavgPM, 'r-o', 'LineWidth', 2)
title('Average Delay/Hops', 'FontSize', 20)
xlabel('Number of Hops', 'FontSize', 18)
ylabel('Average Delay (ms)', 'FontSize', 18)
%legend({'Mon' 'Tue' ' Wed' 'Thu' 'Fri'})
legend({'Path 1'})


figure(3)
hopPlot = [length(mondayHopAM) length(tuesdayHopAM) length(wednesdayHopAM) length(thursdayHopAM) length(fridayHopAM);...
           length(mondayHopAF) length(tuesdayHopAF) length(wednesdayHopAF) length(thursdayHopAF) length(fridayHopAF);...
           length(mondayHopPM) length(tuesdayHopPM) length(wednesdayHopPM) length(thursdayHopPM) length(fridayHopPM)];
% hopPlot = [length(mondayHopAM) length(tuesdayHopAM) length(wednesdayHopAM) length(thursdayHopAM) length(fridayHopAM);...
%            length(mondayHopPM) length(tuesdayHopPM) length(wednesdayHopPM) length(thursdayHopPM) length(fridayHopPM)];
bar(hopPlot)
ylim([0 15])
title('Average Hops Number', 'FontSize', 20)
ylabel('Number of Hops', 'FontSize', 20)
%set(gca,'xticklabel',{'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'});
set(gca,'xticklabel',{'Morning', 'Afternoon', 'Night'});
legend({'Mon' 'Tue' ' Wed' 'Thu' 'Fri'})
%pathf = [length(mondayHop), length(tuesdayHop), length(wednesdayHop), length(thursdayHop), length(fridayHop)];

%% CDNs Analysis
% America Servers
Americatot = [13 3 2 4 3 1 31];
explode = [13 3 2 4 3 1 31];
figure(1)
pie(Americatot, explode)
legend({'Akamai' 'Amazon AWS' 'Cloudfront' 'Fastly' 'Cloudfare' 'PhiCDN' 'Other'})
title('America Servers Using CDN')

% Asia Servers
Asiatot = [5 1 13];
explode = [5 1 13];
figure(2)
pie(Asiatot, explode)
legend({'Akamai' 'Amazon AWS' 'Other'})
title('Asia Servers Using CDN')

% Europe Servers
Europetot = [9 1 1 1 12];
explode = [9 1 1 1 12];
figure(3)
pie(Europetot, explode)
legend({'Akamai' 'Cloudfront' 'CDN-Tech' 'MaxCDN' 'Other'})
title('Europe Servers Using CDN')

%% Avg Hops and Avg Delay Box Plots
clear all
close all
clc

amerAF_avgH = [10 4 7 7 12 10 10 6 10 9 11 9 6 14 11 9 17 7 18 8 7 11 7 7 7 9 10 10 20 8 10 7 8 9 14 10 11 11 9 15 12 20 14 6 6 10 10 11 8 10 10 9 11];
amerAF_avgD = [10 1 25 6 24 8 7 2 9 6 7 6 12 53 11 6 35 12 47 11 6 67 6 6 9 6 111 42 34 29 43 6 7 20 23 24 11 21 17 26 28 55 51 2 4 32 37 34 6 49 55 13 42];
amerAM_avgH = [10 4 7 7 12 10 10 6 10 9 10 9 6 14 11 9 17 7 18 8 7 10 7 7 7 9 10 11 20 10 10 7 8 9 14 10 11 11 12 16 12 20 14 6 6 11 10 12 8 11 10 9 11];
m = median(amerAM_avgH);
amerAM_avgD = [10 1 28 6 21 6 6 2 7 6 6 6 13 55 9 6 35 6 57 9 6 17 6 6 9 6 108 43 35 23 33 6 7 19 23 28 9 22 19 23 28 55 51 2 2 30 29 42 6 30 28 13 41];
amerPM_avgH = [11 4 7 8 11 10 10 6 11 9 11 9 7 14 12 8 17 7 19 9 7 14 8 7 8 9 10 12 21 10 14 8 8 6 14 10 11 11 12 15 12 21 14 6 6 12 12 12 9 12 15 9 15];
amerPM_avgD = [12 1 25 6 21 6 6 2 19 7 6 6 12 52 12 6 35 6 55 9 6 53 6 9 10 6 107 75 34 83 96 6 7 9 23 59 9 27 61 23 28 55 50 2 2 64 67 57 6 72 97 13 89]; 

asiaAF_avgH = [12 11 14 14 10 12 12 10 14 10 10 14 12 14 12 16 14 16 17];
asiaAF_avgD = [195 71 164 62 39 55 180 42 241 51 39 94 194 256 247 270 283 283 258];
asiaAM_avgH = [13 10 15 14 10 11 13 9 14 10 11 14 12 14 12 16 14 15 17];
asiaAM_avgD = [195 53 195 66 19 27 184 20 242 22 28 93 192 256 252 270 292 280 265];
asiaPM_avgH = [12 11 12 14 12 11 11 11 14 12 11 14 12 15 12 15 14 15 17];
asiaPM_avgD = [198 78 117 49 71 111 145 86 243 63 28 93 191 253 239 274 282 276 253];

euroAF_avgH = [9 7 8 15 9 13 12 16 14 14 21 19 10 19 10 16 10 10 13 9 12 9 10 10];
euroAF_avgD = [28 58 29 114 28 97 106 125 101 102 101 105 96 147 28 145 35 38 108 16 94 43 21 11];
euroAM_avgD = [35 21 16 113 19 98 107 125 105 102 98 106 96 149 32 140 22 23 109 10 92 16 8 14];
euroAM_avgH = [10 7 9 15 10 13 12 16 14 14 21 19 10 18 11 15 11 11 13 8 12 9 10 11];
euroPM_avgH = [9 7 9 15 9 14 12 17 14 15 22 20 11 18 10 17 12 9 13 9 12 11 10 11];
euroPM_avgD = [50 23 30 112 29 97 106 126 104 102 99 104 96 149 48 142 70 49 110 8 94 55 8 52];

americagroupH = [amerAM_avgH.' amerAF_avgH.' amerPM_avgH.'];
asiagroupH = [asiaAM_avgH.' asiaAF_avgH.' asiaPM_avgH.'];
europegroupH = [euroAM_avgH.' euroAF_avgH.' euroPM_avgH.'];

% Results of hops analysis
figure(1)
subplot(3,1,1)
boxplot(americagroupH, 'Labels', {'Morning', 'Afternoon', 'Night'})
title('America Weekly Hops Average', 'FontSize', 12)
ylabel('Hops Average')

subplot(3,1,2)
boxplot(asiagroupH, 'Labels', {'Morning', 'Afternoon', 'Night'})
title('Asia Weekly Hops Average', 'FontSize', 12)
ylabel('Hops Average')

subplot(3,1,3)
boxplot(europegroupH, 'Labels', {'Morning', 'Afternoon', 'Night'})
title('Europe Weekly Hops Average', 'FontSize', 12)
ylabel('Hops Average')


americagroupD = [amerAM_avgD.' amerAF_avgD.' amerPM_avgD.'];
asiagroupD = [asiaAM_avgD.' asiaAF_avgD.' asiaPM_avgD.'];
europegroupD = [euroAM_avgD.' euroAF_avgD.' euroPM_avgD.'];

% Results of delay analysis
figure(2)
subplot(3,1,1)
boxplot(americagroupD, 'Labels', {'Morning', 'Afternoon', 'Night'})
ylabel('Delay Average')
title('America Weekly Delay Average', 'FontSize', 12)

subplot(3,1,2)
boxplot(asiagroupD, 'Labels', {'Morning', 'Afternoon', 'Night'})
ylabel('Delay Average')
title('Asia Weekly Delay Average', 'FontSize', 12)

subplot(3,1,3)
boxplot(europegroupD, 'Labels', {'Morning', 'Afternoon', 'Night'})
ylabel('Delay Average')
title('Europe Weekly Delay Average', 'FontSize', 12)
%% 
clear all; 
close all;

% amer33 = [33,33,33];
% %aa66 = zeros();
% for i = 1:22
%     amer66(i) = 22;
% end
% 
% for j = 1:1970
%     amer100(j) = 100;
% end

% asia33 = [33,33,33];
% for k = 1:29
%     asia33(k) = 33;
% end

% for i = 1:42
%     amer66(i) = 66;
% end
% 
% for j = 1:1970
%     amer100(j) = 100;
% end
%%
clear all, close all, clc;
amerAMsendR = 99;
amerAFsendR = 95;
amerPMsendR = 99;

asiaAMsendR = 87;
asiaAFsendR = 79;
asiaPMsendR = 89;

euroAMsendR = 97; 
euroAFsendR = 94;
euroPMsendR = 97;

sendrate = [amerAMsendR asiaAMsendR euroAMsendR; amerAFsendR asiaAFsendR euroAFsendR; amerPMsendR asiaPMsendR euroPMsendR];
bar(sendrate)
set(gca,'xticklabel',{'Morning', 'Afternoon', 'Night'});
legend({'America' 'Asia' ' Europe'})
ylabel('Percent send rate', 'FontSize', 12)
title('Send Rate', 'FontSize', 14)
