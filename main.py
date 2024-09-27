from bs4 import BeautifulSoup
import requests
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
#gets ticker symbols of s&p500 wiki
def get_ticker():
    webResponse = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    
    soup = BeautifulSoup(webResponse.content, "html.parser")
    # Find the table containing the list of S&P 500 companies
    table = soup.find("table", {"class": "wikitable sortable"})

    # Extract the rows from the table
    rows = table.find_all("tr")

    # Loop through the rows and extract the company ticker
    sp500_tickers = []
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all("td")
        if len(cells) >0:
            ticker = cells[0].text.strip()
            sp500_tickers.append(ticker)

    return sp500_tickers


def get_company():
    webResponse = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    soup = BeautifulSoup(webResponse.content, "html.parser")
    # Find the table containing the list of S&P 500 companies
    table = soup.find("table", {"class": "wikitable sortable"})

    # Extract the rows from the table
    rows = table.find_all("tr")

    # Loop through the rows and extract the company ticker
    sp500_companies = []
    for row in rows[1:]:  # Skip the header row
        cells = row.find_all("td")
        if len(cells) >0:
            company_name = cells[1].text.strip()
            sp500_companies.append(company_name)

    return sp500_companies

def get_ticker_earnings(tickers,num):
    count = 0
    for ticker, company in zip(tickers, companies):
        count = count + 1
        #IMPLEMENT YFINANCE BELOW
        #Num of companies up to 500 for s&p 500
        if count > num:
            break
        yfin = yf.Ticker(ticker)
        st.text("$"+ticker +"   Company name: " + company)
        st.write(yfin.earnings_dates)
    return ""

def get_chart_history(tickers,num):
    #IMPLEMENT MATPLOTLIB
    count = 0
    for ticker, company in zip(tickers, companies):
        count = count + 1
        #IMPLEMENT YFINANCE BELOW
        #Num of companies up to 500 for s&p 500
        if count > num:
            break
        yfin = yf.Ticker(ticker)
        data = yfin.history(interval="1d", period = "1mo")
        # print('=========================', data.shape)
        # print(data.index.shape)
        # data['Close'][-1]

        plt.figure(figsize=(14, 6))  # Set figure size
        plt.plot(data.index, data['Close'])  # Plot the closing price
        plt.title(f"{ticker} - {company} Closing Price History")  # Set title
        plt.xlabel("Date")  # Set x-axis label
        plt.ylabel("Closing Price ($)")  # Set y-axis label
        #plt.grid(True)  # Enable grid
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        st.pyplot(plt)  # Display the plot in Streamlit
    return ""

def get_options(tickers, num):
    count = 0
    for ticker, company in zip(tickers, companies):
        count = count+1
        #Num of companies up to 500 for s&p 500
        if count > num:
            break
        yfin = yf.Ticker(ticker)
        st.text("$"+ticker +"   Company name: " + company)
        st.write(yfin.options)
    return ""

def get_dividends(tickers, num):
    count = 0
    for ticker, company in zip(tickers, companies):
        count = count+1
        #IMPLEMENT YFINANCE BELOW
        #Num of companies up to 500 for s&p 500
        if count > num:
            break
        yfin = yf.Ticker(ticker)
        st.text("$"+ticker +"   Company name: " + company)
        st.write(yfin.dividends[::-1])
    return ""

tickers = get_ticker()
companies = get_company()

st.title("S&P 500 Scraper")    
st.markdown(''':orange[Scrapes S&P 500 companies]''')
number_input = st.slider("Enter number of companies in the S&P 500 to scrape ", min_value = 0, max_value = 500, value = 0, step = 1)
user_input = st.text('Click a scrape function of S&P 500 to use:')

earnings = st.button(":green[Earnings]")
price = st.button(":blue[Price Chart]")
options = st.button(":red[Options Expirations]")
dividends = st.button(":rainbow[Dividends]")
specific = st.sidebar.button(":violet[Specific Ticker]")


if(earnings):

    st.write(get_ticker_earnings(tickers,number_input))

elif(price):

    st.write(get_chart_history(tickers,number_input))

elif(options):
    
    st.write(get_options(tickers,number_input))

elif(dividends):
    
    st.write(get_dividends(tickers,number_input))
elif not(earnings or dividends or options or price or specific):

    st.text("Click a function to get started")

elif specific:
        
        specific_options = ['Earnings', 'Price Chart', 'Options Expirations', 'Dividends']
        selected_function = st.sidebar.radio('Select function for the ticker:', specific_options)

        if(selected_function == 'Earnings'):

            specific_input = st.sidebar.text_input("Enter ticker to find its earnings")
            if specific_input:
                st.sidebar.text(f"You entered: {specific_input}")
                yfin = yf.Ticker(specific_input)
                if len(yfin.earnings_dates) > 0:
                    st.write(yfin.earnings_dates)
            else:
                st.write("Enter a ticker.")

        elif(selected_function == 'Price Chart'):

            specific_input = st.text_input("Enter ticker to find its price chart")
            yfin = yf.Ticker(specific_input)
            st.write(yfin.history)
                     
        elif(selected_function == 'Options Expirations'):

            specific_input = st.text_input("Enter ticker to find its options expirations")
            yfin = yf.Ticker(specific_input)
            st.write(yfin.options)

        elif(selected_function == 'Dividends'):

            specific_input = st.text_input("Enter ticker to find its dividends")
            yfin = yf.Ticker(specific_input)
            st.write(yfin.dividends)
        #earnings2 = st.button(":green[Specific Earnings]")
        #price2 = st.button(":blue[Specific Price Chart]")
        #options2 = st.button(":red[Specific Options Expirations]")
        #dividends2 = st.button(":rainbow[Specific Dividends]")


