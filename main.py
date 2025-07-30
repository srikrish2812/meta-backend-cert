def main():
    import yfinance as yf
    dat = yf.Ticker("NVDA")
    print(dat.info)


if __name__ == "__main__":
    main()
