# Import necessary libraries and custom functions from external modules
from gfunctions import *
from Afunctions import *
import json
import numpy as np
import openai
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import streamlit as st
from scipy import stats
import datetime
from dateutil.parser import parse
import spacy
import re
nlp = spacy.load('en_core_web_sm')

# Set OpenAI API key
openai.api_key = "your_key"


# Define a dictionary of available custom functions
availableFunctions = {
    'getStockPrice': getStockPrice,
    'calculateSMA': calculateSMA,
    'calculateEMA': calculateEMA,
    'calculateRSI': calculateRSI,
    'calculateMACD': calculateMACD,
    'plotStockPrice': plotStockPrice,
    'rollingVolatility': rollingVolatility,
    'sharpeRatio': sharpeRatio,
    'betaRatio': betaRatio,
    'valueAtRisk': valueAtRisk,
    'annualizedPerformance': annualizedPerformance,
    'information_ratio': information_ratio,
    'rolling_correlation': rolling_correlation,
    'maximum_drawdown': maximum_drawdown,
    'omega_ratio': omega_ratio,
    'r_squared': r_squared,
    'relative_return': relative_return,  # New function
    'compare_performance': compare_performance,  # New function
    'compare_risk': compare_risk,  # New function
    'volatility': volatility,  # New function
    'relative_volatility': relative_volatility,  # New function
    'compare_volatility': compare_volatility,  # New function
    'compare_relative_volatility': compare_relative_volatility,  # New function
    'compare_rolling_volatility': compare_rolling_volatility,  # New function
}

# Define a dictionary of available plots associated with functions
availablePlots = {
    'plotStockPrice': 'stock.png',
    'rollingVolatility': 'rolling_volatility.png',
}

# Check if 'messages' is not in Streamlit session state, and initialize it if not present
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

# Set the title for the Streamlit app
st.title('StockSage: Stock Analysis Assistant')

# Get user input from a text input field
user_input = st.text_input('Your input:')


# if user_input:
#     try:

#         user_requests = re.split(
#             r'\s*(?:then|after that|and|,|:|;|-|/|than|after|after this)\s*', user_input)

#         for request in user_requests:

if user_input:
    try:
        # Check if the user input contains keywords for comparing performance or risk or volatility
        if 'compare' in user_input or 'riskier' in user_input or 'performed better' in user_input or 'compared' in user_input or 'comparison' in user_input or 'superior' in user_input or 'better' in user_input or 'versus' in user_input or 'vs' in user_input or 'between' in user_input:
            requests = [user_input]
        else:
            # Split the user input into multiple requests using regular expression
            requests = re.split(
                r'\s*(?:then|after that|and|,|:|;|-|/|than|after|after this)\s*', user_input)

        # Process each request
        for request in requests:
            st.session_state['messages'].append(
                {'role': 'user', 'content': request.strip()})

            response = openai.ChatCompletion.create(
                model='gpt-3.5-turbo-0613',
                messages=st.session_state['messages'],
                functions=functions,
                function_call='auto'
            )

            response_message = response['choices'][0]['message']

            if response_message.get('function_call'):
                function_name = response_message['function_call']['name']
                function_args = json.loads(
                    response_message['function_call']['arguments'])

                args_dict = {}
                for arg_name, arg_value in function_args.items():
                    args_dict[arg_name] = arg_value
                function_to_call = availableFunctions[function_name]
                function_response = function_to_call(**args_dict)
                st.session_state['messages'].append(response_message)
                st.session_state['messages'].append(
                    {
                        'role': 'assistant',
                        'name': function_name,
                        'content': function_response
                    }
                )
                second_response = openai.ChatCompletion.create(
                    model='gpt-3.5-turbo-0613',
                    messages=st.session_state['messages']
                )

                assistant_message = second_response['choices'][0]['message']
                if 'content' in assistant_message:
                    assistant_content = assistant_message['content']
                    st.code(assistant_content, language='text')

                    st.session_state['messages'].append(
                        {'role': 'assistant', 'content': assistant_content})
                    if function_name in availablePlots:
                        st.image(availablePlots[function_name])
                else:
                    st.text("Assistant's response is missing 'content' key.")
            else:
                st.text(response_message['content'])
                st.session_state['messages'].append(
                    {'role': 'assistant', 'content': response_message['content']})
    except Exception as e:
        raise e
