def one_sample_test(company, ): 
    
    comp_complaints = auto_data[auto_data['Company'] == str(company)]['File No.'].count()
    comp_referrals = auto_data[(auto_data['Disposition'] == 'Refer-Judicial/Attorney')]
    comp_referrals = auto_jud[auto_jud['Company'] == 'GEICO General Insurance Company']['Company'].count()

