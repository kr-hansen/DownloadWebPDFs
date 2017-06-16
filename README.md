# DownloadWebPDFs
Web Scraping code that uses Selenium Python and BeautifulSoup to download and save PDFs

Written to specifically download PDF versions of the Dungeon Master Experience Articles publicly available on the D&D Wizards of the Coast website.

The 2011 articles are compiled in PDF form at this link: https://www.wizards.com/dnd/files/DM_Experience_2011.pdf.  However, more recent articles are not available on the website in a concise form.  Manually saving the PDFs resulted in some odd things since the HTML for the website is a little odd, so I wrote this script to try and make it a little less wonky, though it is still pretty rough and somewhat wonky as pulled from this code.  However, it works!

Uses the Selenium driver and Firefox to open the headings to all of the articles and get the links.  Each page is opened, the HTML is scraped from those pages and the body text of the articles is saved into a PDF format.
