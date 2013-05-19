{
  cout << "Starting WordCount.C" << endl;
	
  // --------------- Change Styles --------------- \	\
	
  //gROOT->LoadMacro("/Applications/tbAnalysis/atlasstyle-00-03-05/AtlasStyle.C");
  //SetAtlasStyle();
  
  //gStyle->SetPadTickX(0);
  //gStyle->SetPadRightMargin(0.16);
  //gStyle->SetPadGridX(1); // grids
  //gStyle->SetPadGridY(1);
	
  TGaxis::SetMaxDigits(6); //Outputs word count total properly
	
  // ---------------------- Projected Finish Lines  ---------------------------- \ \
	
  TCanvas *c1 = new TCanvas("c1","Thesis Word Count",800, 600);
  Double_t x_sept[2], x_aug[2], x_july[2], y[2];
  Float_t offset = 43200*2; // Offset for correct x-axis range. In seconds.
  
  TDatime da0(2013,04,15,12,00,00);		// Start of counting
  TDatime da_july(2013,07,31,12,00,00);	// Estimated end-dates
  TDatime da_aug(2013,08,31,12,00,00);
  TDatime da_sept(2013,09,30,12,00,00);
  
  x_sept[0] = da0.Convert();
  x_sept[1] = da_sept.Convert();
  
  y[0] = 0;
  y[1] = 25000;
  
  gr_sept = new TGraph(2,x_sept,y);
  TAxis* xax = gr_sept->GetXaxis();
  TAxis* yax = gr_sept->GetYaxis();
  
  xax->SetRangeUser(da0.Convert()-offset,da_sept.Convert()+offset);
  
  gr_sept->SetTitle("");
  xax->SetTitle("Date");
  yax->SetTitle("Word Count");
  
  yax->SetTitleOffset(1.5);
  
  c1->SetRightMargin(1);
  
  xax->SetTimeDisplay(1);
  xax->SetNdivisions(-403);
  xax->SetTimeFormat("%d\/%m\/%Y");
  xax->SetTimeOffset(0,"gmt");
  
  gr_sept->SetLineWidth(2);
  gr_sept->SetLineColor(kRed+1);
  
  gr_sept->Draw("AC");
  
  // --- August Line --- \			\
  
  x_aug[0] = da0.Convert();
  x_aug[1] = da_aug.Convert();
  
  gr_aug = new TGraph(2,x_aug,y);
  
  gr_aug->SetLineWidth(2);
  gr_aug->SetLineColor(kOrange+1);
  
  gr_aug->Draw("same");
  
  // --- July Line --- \			\
  
  x_july[0] = da0.Convert();
  x_july[1] = da_july.Convert();
  
  gr_july = new TGraph(2,x_july,y);
  
  gr_july->SetLineWidth(2);
  gr_july->SetLineColor(kGreen+1);
  
  gr_july->Draw("same");
  
  
  // ------------------ My Word Count -------------------- \	\
  
  int n = 3; //Update me each time you add a new word count
  
  TDatime *WC[n];
  WC[0]  = new TDatime (2013,05,01,12,00,00);	//Date
  WC[1]  = new TDatime (2013,05,01,17,08,21);
  
  Double_t i[n], j[n];
  for(int a=0; a<n; a++){
    i[a] = WC[a]->Convert();
  }
  j[0]  = 0;
  j[1]  = 9261;
  
  wc = new TGraph(n,i,j);
  wc->SetLineWidth(2);
  wc->Draw("same");
  
  c1->Update();
  
  // ------------------ Legend -------------------- \	\
  leg = new TLegend(0.6, 0.25, 0.8, 0.5);
  leg -> SetFillColor(0);			// White Background
  leg -> SetBorderSize(0);
  //leg -> SetHeader("Word Count");
  leg -> AddEntry(wc, "Current Word Count", "l");
  leg -> AddEntry(gr_july, "Late July finish", "l");
  leg -> AddEntry(gr_aug, "Late August finish", "l");
  leg -> AddEntry(gr_sept, "Late September finish", "l");
  
  leg -> Draw();
  
  // ------------------ Print -------------------- \	\
  c1 -> Print("WordCount.png");
}

