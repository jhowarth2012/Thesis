from ROOT import *
from counts import word_count,page_count
from array import *

gROOT.SetStyle("Plain")
x = []
y_words = []
y_pages = []

for i in word_count:
    x.append(i[0])
    y_words.append(i[1])

for i in page_count:
    y_pages.append(i[1])

print x
print y_words
print y_pages

xprime       = array('d', x)
y_wordsprime = array('d', y_words)
y_pagesprime = array('d', y_pages)

wordcount = TGraph(len(x),xprime, y_wordsprime)
pagecount = TGraph(len(x),xprime, y_pagesprime)

c1 = TCanvas()
pad = TPad("pad","",0,0,1,1);
#pad.SetFillColor(42);
pad.SetFillColor(0);
pad.SetGrid();
pad.Draw();
pad.cd();

#draw a frame to define the range
hr = c1.DrawFrame(0,0,100,50000);
hr.SetXTitle("Day");
hr.SetYTitle("Word Count");
hr.GetYaxis().SetLabelSize(0.03)
hr.GetYaxis().SetTitleOffset(1.2);
#pad.GetFrame().SetFillColor(21);
#pad.GetFrame().SetBorderSize(12);
pad.GetFrame().SetFillColor(0);
pad.GetFrame().SetBorderSize(0);

wordcount.SetLineWidth(2)
wordcount.SetMarkerSize(1)
wordcount.SetMarkerStyle(22)
pagecount.SetLineWidth(2)
pagecount.SetLineColor(4)
pagecount.SetMarkerSize(1)
pagecount.SetMarkerStyle(23)
pagecount.SetMarkerColor(4)

wordcount.Draw("PL")

#create a transparent pad drawn on top of the main pad
c1.cd();
overlay = TPad("overlay","",0,0,1,1);
overlay.SetFillStyle(4000);
overlay.SetFillColor(0);
overlay.SetFrameFillStyle(4000);
overlay.Draw();
overlay.cd();
xmin = pad.GetUxmin();
ymin = pad.GetUymin();
xmax = pad.GetUxmax();
ymax = 250;
hframe = overlay.DrawFrame(xmin,ymin,xmax,ymax);
hframe.GetXaxis().SetLabelOffset(99);
hframe.GetYaxis().SetLabelOffset(99);
hframe.SetYTitle("Page Count");
hframe.GetYaxis().SetTitleOffset(99);

pagecount.Draw("PL")
      
#Draw an axis on the right side
axis = TGaxis(xmax,ymin,xmax, ymax,ymin,ymax,510,"+L");
axis.SetLineColor(kBlue);
axis.SetLabelColor(kBlue);
axis.Draw();

raw_input("WAIT")
