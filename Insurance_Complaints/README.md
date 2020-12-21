# Insurance Complaints
## *Balancing profitability and quality* 

# Background/Motivation/Prior Research
As a business owner, I know that some of the best service improvements and staff growth opportunities have come from clients who were displeased with the status quo. While it's easy to think of complaints in a negative light, they allow us to assess financial risks and to work towards a better product than the competition. 

In the U.S., there is significant debate around the cost and quality of private insurers.  Public policy might impose changes to insurers in the future, but the current system is worth exploring from a business perspective. By looking at insurance company complaints as one performance metric, my aim is to determine if insurers are avoiding potentially cost-laden scenarios. 

# Data & Technology
The dataset looks at insurance company complaints in the state of Connecticut and was obtained from Kaggle. 

The following technologies were utilized: 
- pandas
- matplotlib, seaborn
- SciPy

# Methodology
## *Exploratory Data Analysis*
Before starting EDA, I first checked the Insurance Complaints dataset for null values, duplicate entries, and outliers. In my [initial analysis](https://github.com/HuebnerC/Insurance_Complaints/blob/master/Insurance_Complaints/ins_complaints.ipynb), I noticed that there were many duplicate entries, and that Anthem had more than twice the number of complaints than the next several insurers. Because the number of complaints could be attributed to sheer company size, I used revenue from premiums to normalize the data for company size. 

Because the dataset contains over 600 insurance companies, many of which have only one complaint, I looked at the ten companies with the highest number of complaints, and from those selected a subset of insurers with high visibility in the US. 

I grouped the insurers by policy type, as an auto policy will be handled differently than a life policy, for example, and explored data relevant to auto and to health insurers. 

I explored a number of questions: 
- How many complaints were associated with a recovery payout? 
- Did the duration of complaints change predictably depending on the reason for complaint, company position, etc?
- How many cases were referred to legal counsel and what was the outcome of those cases? 

## *Consulting with Industry Experts*
After my initial EDA, I spoke with an insurance lawyer to refine my research question. Chadwell Murley works for a large, well-known insurer defending the company against lawsuits brought on by the insured. I asked Chadwell to take a look at the reasons and subreasons for complaints and weigh in on which might be more likely to result in significant recovery amounts and legal fees for the insurer. 

Chadwell explained that in the state where he practices law, there are certain things that are nearly impossible to litigate against and that there are certain things would fall under treble damages, a term that indicates there is a statute that would allow a court to award three times the actual compensation amount to the plaintiff. For those two reasons, he suggested I focus on unsatisfactory settlement, premium notice, medical necessity, actual cash value, and unreasonable delay. 

## *Understanding the Role of Subsidiaries*
I did not lump insurers from the same parent company together. Insurers often have subsidiary companies that operate under different coverage policies and risk pools. For example, GEICO General Insurance underwrites for low-risk drivers, GEICO Indemnity for medium risk, and GEICO Casualty for high-risk. This information is typically a matter of internal policy, and is scantly available to the public.

From the Washington Post, these classifications are describe as looing "at an applicant from three perspectives: driving record, personal characteristics and the vehicles to be insured. It appears to seek information beyond a basic application and does not address many standard questions such as miles driven, type of car and gender of driver."
[The Color of Your Collar, and Other Ways Geico Rates Your Risk](https://www.washingtonpost.com/archive/business/2006/03/26/the-color-of-your-collar-and-other-ways-geico-rates-your-risk/92e880f5-a43e-4da2-8595-98acc40d10a3/)

While I was able to find this information for GEICO, I was not able to find this information for other companies. Instead of subsidiaries being designated by risk category, they were designated based on with whom the insured contracts with - a local agent or the parent company. More research needed on this. 

# Research Questions
- What can insurance complaints tell us about how insurers process claims?
- Are insurers mitigating the financial risk associated with a lawsuit by handling insurance claims appropriately?
- Can complaints be used as a metric for investors?

# Statistical testing
*Research question: Are complaint cases being referred to legal?*

I thought perhaps a high complaint rate would result in an above-average rate of referral to legal. I looked at GEICO General to see if their legal referral rate is above average. 

I assumed a binomial distribution with n= number of complaints for that company and a probability of 9%. I set the alpha value at 0.05. 
Nationally, about 5% of auto claims wind up in court. I used a more conservative since these are complaints, not claims, and calculated this probability using the overall rate of referral to legal in the dataset.

# Conclusions
Regardless of the number of complaints a company received, the majority of complaints were centered around high-risk actions, like claim denial or delay. While this study does not explore causation or the actual claims that resulted in complaints, insurers could explore internal policies that would help them reduce the number of complaints in these areas. 

Insurers could use this information to refine their internal processes or to compare company performance against that of competitors. Another application would be for a parent company to compare the rate at which subsidiaries refer cases to legal counsel in order to adjust premiums. However, this should be undertaken with great consideration and caution, as there is a possibility for discrimination and has been the subject of [discrimination lawsuits](https://www.govinfo.gov/content/pkg/USCOURTS-mnd-0_06-cv-01281/pdf/USCOURTS-mnd-0_06-cv-01281-0.pdf) in the past.

# Considerations for further study
- In the future, it would be interesting to see if complaint data is in line with claims resolution data. 
- Complaint data vs online customer reviews
- Complaint data vs employer reviews
- Complaint data vs demographics of insured for each company
- Complaint data vs fraud indicators
- Comparison across states 

# Citations:

* Published Financials used for normalizing complaint data:
    * [Anthem](https://ir.antheminc.com/news-releases/news-release-details/anthem-reports-fourth-quarter-and-full-year-2018-results#:~:text=Operating%20Revenue%3A%20Operating%20revenue%20was,in%20the%20prior%20year%20quarter.)
    * [United](https://www.unitedhealthgroup.com/viewer.html?file=/content/dam/UHG/PDF/investors/2018/UNH-Q4-2018-Form-10-K.pdf)
    * [Cigna](https://www.cigna.com/static/www-cigna-com/docs/about-us/investor-relations/quarterly-reports-and-sec-filings/cigna-corp-fourth-quarter-2017-release.pdf)
    * [Aetna](https://www.sec.gov/Archives/edgar/data/1122304/000112230418000027/form10-k.htm#sEB34082FF113B9BC54FC92AECD69AA97)
    * [Allstate F&C](https://www.sec.gov/Archives/edgar/data/899051/000089905119000007/allcorp-12311810xk.htm)
    * [Allstate](https://www.allstate.com/resources/allstate/attachments/annual-report/allstate-prosperity-report-combo-book-2018.pdf)
    * [GEICO](https://www.berkshirehathaway.com/2018ar/2018ar.pdf)
    * [State Farm](https://static1.st8fm.com/en_US/downloads/2018-annual-report.pdf)
* Average rate auto claims go to litigation 
    * [Legal News] https://www.jdsupra.com/legalnews/what-are-your-chances-of-winning-a-car-48036/#:~:text=Remember%2C%20statistically%20speaking%2C%2095%20percent,in%20favor%20of%20the%20plaintiff.
