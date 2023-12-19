functions = [


    {
        'name': 'volatility',
        'description': 'Calculates the volatility of a given stock over a specified date range.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for the company (for example, AAPL for Apple).'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for the date range (YYYY-MM-DD). If not provided, defaults to one year ago.'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for the date range (YYYY-MM-DD). If not provided, defaults to today.'
                }
            },
            'required': ['ticker']
        }
    },

    {
        'name': 'relative_volatility',
        'description': 'Calculates the relative volatility between two given stocks over a specified date range.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker1': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for the first company.'
                },
                'ticker2': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for the second company.'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for the date range (YYYY-MM-DD). If not provided, defaults to one year ago.'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for the date range (YYYY-MM-DD). If not provided, defaults to today.'
                }
            },
            'required': ['ticker1', 'ticker2']
        }
    },

    {
        'name': 'compare_volatility',
        'description': 'Compares the volatility of two or more stocks over a specified date range.',
        'parameters': {
            'type': 'object',
            'properties': {
                'tickers': {
                    'type': 'array',
                    'items': {'type': 'string'},
                    'description': 'An array of stock ticker symbols for the companies to compare (for example, ["AAPL", "MSFT", "GOOG"]).'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for the date range (YYYY-MM-DD). If not provided, defaults to one year ago.'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for the date range (YYYY-MM-DD). If not provided, defaults to today.'
                }
            },
            'required': ['tickers']
        }
    },



    {
        'name': 'compare_relative_volatility',
        'description': 'Compares the relative volatility of two or more stocks over a specified date range.',
        'parameters': {
            'type': 'object',
            'properties': {
                'tickers': {
                    'type': 'array',
                    'items': {'type': 'string'},
                    'description': 'An array of stock ticker symbols for the companies to compare (for example, ["AAPL", "MSFT", "GOOG"]).'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for the date range (YYYY-MM-DD). If not provided, defaults to one year ago.'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for the date range (YYYY-MM-DD). If not provided, defaults to today.'
                }
            },
            'required': ['tickers']
        }
    },


    {
        'name': 'compare_rolling_volatility',
        'description': 'Compares the rolling volatility of two or more stocks over a specified date range.',
        'parameters': {
            'type': 'object',
            'properties': {
                'tickers': {
                    'type': 'array',
                    'items': {'type': 'string'},
                    'description': 'An array of stock ticker symbols for the companies to compare (for example, ["AAPL", "MSFT", "GOOG"]).'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for the date range (YYYY-MM-DD). If not provided, defaults to one year ago.'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for the date range (YYYY-MM-DD). If not provided, defaults to today.'
                }
            },
            'required': ['tickers']
        }
    },

    {
        'name': 'compare_performance',
        'description': 'Compares the performance of two or more tickers over a specified date range.',
        'parameters': {
            'type': 'object',
            'properties': {
                'tickers': {
                    'type': 'array',
                    'items': {'type': 'string'},
                    'description': 'An array of stock ticker symbols for the companies to compare (for example, ["AAPL", "MSFT", "GOOG"]).'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for the date range (YYYY-MM-DD). If not provided, defaults to one year ago.'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for the date range (YYYY-MM-DD). If not provided, defaults to today.'
                }
            },
            'required': ['tickers']
        }
    },
    {
        'name': 'compare_risk',
        'description': 'Compares the risk of two or more tickers over a specified date range.',
        'parameters': {
            'type': 'object',
            'properties': {
                'tickers': {
                    'type': 'array',
                    'items': {'type': 'string'},
                    'description': 'An array of stock ticker symbols for the companies to compare (for example, ["AAPL", "MSFT", "GOOG"]).'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for the date range (YYYY-MM-DD). If not provided, defaults to one year ago.'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for the date range (YYYY-MM-DD). If not provided, defaults to today.'
                }
            },
            'required': ['tickers']
        }
    },


    {
        'name': 'relative_return',
        'description': 'Calculates the relative return of a stock compared to a benchmark.',
        'parameters': {
                'type': 'object',
                'properties': {
                    'ticker': {
                        'type': 'string',
                        'description': 'The stock ticker symbol for the asset.'
                    },
                    'benchmark_ticker': {
                        'type': 'string',
                        'description': 'The stock ticker symbol for the benchmark.'
                    },
                    'start_date': {
                        'type': 'string',
                        'description': 'The start date for the period (YYYY-MM-DD).'
                    },
                    'end_date': {
                        'type': 'string',
                        'description': 'The end date for the period (YYYY-MM-DD).'
                    }
                },
            'required': ['ticker', 'benchmark_ticker']
        }
    },

    {
        'name': 'getStockPrice',
        'description': 'Gets the latest stock price given the ticker symbol of a company.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple).'

                },
                "date": {
                    'type': 'string',
                    'description': 'The date for which the stock price is required (YYYY-MM-DD).'
                },
                'year': {
                    'type': 'string',
                    'description': 'The year for which the stock price is required (YYYY).'

                }
            },
            'required': ['ticker']
        }
    },
    {
        'name': 'calculateSMA',
        'description': 'Calculate the simple moving average for a given stock ticker and a window.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple).'

                },
                'window': {
                    'type': 'integer',
                    'description': 'The timeframe to consider when calculating the SMA'
                }
            },
            'required': ['ticker', 'window'],
        },

    },
    {
        'name': 'calculateEMA',
        'description': 'Calculate the exponential moving average for a given stock ticker and a window.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple).'

                },
                'window': {
                    'type': 'integer',
                    'description': 'The timeframe to consider when calculating the EMA'
                }
            },
            'required': ['ticker', 'window'],
        },
    },
    {
        'name': 'calculateRSI',
        'description': 'Calculate the RSI for a given stock ticker.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple).'

                }

            },
            'required': ['ticker'],
        },
    },
    {
        'name': 'calculateMACD',
        'description': 'Calculate the MACD for a given stock ticker.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (for example AAPL for Apple).'

                },
            },
            'required': ['ticker'],
        },
    },
    {
        'name': 'plotStockPrice',
        'description': 'Plot the stock price for a specified date range given the ticker symbol of a company.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (e.g., AAPL for Apple).'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for plotting the stock price (YYYY-MM-DD).'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for plotting the stock price (YYYY-MM-DD).'
                }
            },
            'required': ['ticker'],
        },
    },
    {
        'name': 'rollingVolatility',
        'description': 'Calculate rolling volatility for a given stock ticker within a date range.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (e.g., AAPL for Apple).'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for calculating volatility (YYYY-MM-DD).'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for calculating volatility (YYYY-MM-DD).'
                }
            },
            'required': ['ticker'],
        },
    },
    {
        'name': 'sharpeRatio',
        'description': 'Calculate the Sharpe ratio for a given stock ticker within a date range.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (e.g., AAPL for Apple).'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for calculating the Sharpe ratio (YYYY-MM-DD).'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for calculating the Sharpe ratio (YYYY-MM-DD).'
                },
                'risk_free_rate': {
                    'type': 'number',
                    'description': 'The risk-free rate used in the Sharpe ratio calculation.'
                }
            },
            'required': ['ticker', 'start_date', 'end_date', 'risk_free_rate'],
        },
    },
    {
        'name': 'betaRatio',
        'description': 'Calculate the beta ratio between two stocks within a date range.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker1': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for the first company (e.g., AAPL for Apple).'
                },
                'ticker2': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for the second company.'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for calculating the beta ratio (YYYY-MM-DD).'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for calculating the beta ratio (YYYY-MM-DD).'
                }
            },
            'required': ['ticker1', 'ticker2'],
        },
    },
    {
        'name': 'valueAtRisk',
        'description': 'Calculate the Value at Risk (VaR) for a given stock ticker within a date range.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (e.g., AAPL for Apple).'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for calculating VaR (YYYY-MM-DD).'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for calculating VaR (YYYY-MM-DD).'
                },
                'confidence_interval': {
                    'type': 'number',
                    'description': 'The confidence interval for VaR calculation.'
                }
            },
            'required': ['ticker', 'start_date', 'end_date', 'confidence_interval'],
        },
    },
    {
        'name': 'information_ratio',
        'description': 'Measures the active return of a portfolio divided by the tracking error.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker1': {
                    'type': 'string',
                    'description': 'The ticker symbol for the first asset.'
                },
                'ticker2': {
                    'type': 'string',
                    'description': 'The ticker symbol for the second asset.'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for the analysis (YYYY-MM-DD).'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for the analysis (YYYY-MM-DD).'
                }
            },
            'required': ['ticker1', 'ticker2'],
        },
    },
    {
        'name': 'rolling_correlation',
        'description': 'Calculates the rolling correlation between two assets.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker1': {
                    'type': 'string',
                    'description': 'The ticker symbol for the first asset.'
                },
                'ticker2': {
                    'type': 'string',
                    'description': 'The ticker symbol for the second asset.'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for the analysis (YYYY-MM-DD).'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for the analysis (YYYY-MM-DD).'
                }
            },
            'required': ['ticker1', 'ticker2'],
        },
    },
    {
        'name': 'maximum_drawdown',
        'description': 'Measures the largest single drop from peak to bottom in the value of a portfolio.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The ticker symbol for the asset.'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for the analysis (YYYY-MM-DD).'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for the analysis (YYYY-MM-DD).'
                }
            },
            'required': ['ticker'],
        },
    },
    {
        'name': 'omega_ratio',
        'description': 'Calculates the omega ratio for an asset.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The ticker symbol for the asset.'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for the analysis (YYYY-MM-DD).'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for the analysis (YYYY-MM-DD).'
                },
                'threshold_return': {
                    'type': 'number',
                    'description': 'The threshold return for the omega ratio calculation.'
                }
            },
            'required': ['ticker', 'start_date', 'end_date', 'threshold_return'],
        },
    },
    {
        'name': 'r_squared',
        'description': 'Measures the percentage of a fund or security\'s movements that can be explained by movements in the benchmark index.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker1': {
                    'type': 'string',
                    'description': 'The ticker symbol for the asset.'
                },
                'ticker2': {
                    'type': 'string',
                    'description': 'The ticker symbol for the benchmark index.'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for the analysis (YYYY-MM-DD).'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for the analysis (YYYY-MM-DD).'
                }
            },
            'required': ['ticker1', 'ticker2', 'start_date', 'end_date'],
        },
    },
    {
        'name': 'annualizedPerformance',
        'description': 'Calculate the annualized performance for a given stock ticker within a date range.',
        'parameters': {
            'type': 'object',
            'properties': {
                'ticker': {
                    'type': 'string',
                    'description': 'The stock ticker symbol for a company (e.g., AAPL for Apple).'
                },
                'start_date': {
                    'type': 'string',
                    'description': 'The start date for calculating annualized performance (YYYY-MM-DD).'
                },
                'end_date': {
                    'type': 'string',
                    'description': 'The end date for calculating annualized performance (YYYY-MM-DD).'
                }
            },
            'required': ['ticker'],
        },
    }
]
