import streamlit as st 
import yfinance as yf 
import pandas as pd


st.title('My favourite Finance Dashboard')

tickers= ('TSLA' ,'AAPL','META','GOOG','NFLX')


dropdown=st.multiselect('Pick your assets', tickers)

start=st.date_input('start', value=pd.to_datetime('2022-01-01'))  ## we need a data time object ; give a default date 
end=st.date_input('End', value=pd.to_datetime('today'))

##  percentage change fucniton 
def relative(df):
	rel=df.pct_change()
	cumret=(1+rel).cumprod() -1       ## culmulative return
	cumret = cumret.fillna(0)
	return cumret


## we need a online data request 
## now it become a return chart 

if len(dropdown)>0: ## in case error 

	# df=yf.download(dropdown, start, end)['Adj Close']
	df=relative(yf.download(dropdown, start, end)['Adj Close'])


	st.header('Return of {}'. format(dropdown))
	st.line_chart(df)

