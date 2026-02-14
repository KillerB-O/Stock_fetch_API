<h1>Stock Fetch API – FastAPI Project</h1>

<p>
A simple and scalable <strong>Stock Price Fetch API</strong> built using 
<strong>FastAPI</strong> and <strong>Yahoo Finance (yfinance)</strong>.
This project allows users to fetch live (near-real-time) stock data using stock symbols.
</p>

<hr>

<h2>Features</h2>
<ul>
    <li>Fetch current stock price</li>
    <li>Open, High, Low, Previous Close</li>
    <li>Market Cap and Currency</li>
    <li>Clean API architecture (Router + Service + Schema)</li>
    <li>Supports Indian and International stocks</li>
    <li>Easy to extend (alerts, database, frontend, etc.)</li>
</ul>

<hr>

<h2>Tech Stack</h2>
<ul>
    <li>Python 3.10+</li>
    <li>FastAPI</li>
    <li>Uvicorn</li>
    <li>yfinance</li>
    <li>Pydantic</li>
</ul>

<hr>

<h2>Project Structure</h2>
<pre>
Stock_fetch_api/
│
├── main.py
├── routers/
│   └── stock.py
├── services/
│   └── stock_service.py
└── schema/
│   └── stock.py

└── requirements.txt
</pre>

<hr>

<h2>Installation</h2>

<h3>1. Clone or Download Project</h3>
<pre>git clone &lt;repo-url&gt;
cd Stock_fetch_API</pre>

<h3>2. Install Dependencies</h3>
<pre>pip install -r requirements.txt</pre>

<hr>

<h2>Running the Server</h2>
<pre>uvicorn main:app --reload</pre>

<p>Open in browser:</p>
<pre>http://127.0.0.1:8000/docs</pre>

<p>This opens Swagger UI where you can test endpoints.</p>

<hr>

<h2>API Endpoint</h2>

<h3>Get Stock Data</h3>
<pre>GET /stock/{symbol}</pre>

<p>Examples:</p>
<pre>
/stock/AAPL
/stock/TSLA
/stock/RELIANCE.NS
</pre>

<hr>

<h2>Stock Symbol Format</h2>
<p>
Yahoo Finance requires <strong>exchange suffixes</strong> for many international stocks.
</p>

<h3>Indian Stocks (NSE &amp; BSE)</h3>
<table>
    <tr>
        <th>Exchange</th>
        <th>Suffix</th>
        <th>Example</th>
    </tr>
    <tr>
        <td>NSE (National Stock Exchange)</td>
        <td>.NS</td>
        <td>RELIANCE.NS</td>
    </tr>
    <tr>
        <td>BSE (Bombay Stock Exchange)</td>
        <td>.BO</td>
        <td>RELIANCE.BO</td>
    </tr>
</table>

<p><strong>Recommended:</strong> Use <code>.NS</code> first for Indian stocks.</p>

<p>Examples:</p>
<pre>
INFY.NS
TCS.NS
SBIN.NS
HDFCBANK.NS
</pre>

<hr>

<h3>US Stocks</h3>
<p>No suffix usually required.</p>
<pre>
AAPL
TSLA
MSFT
GOOGL
</pre>

<hr>

<h3>Other Countries</h3>
<table>
    <tr>
        <th>Country</th>
        <th>Example Symbol</th>
    </tr>
    <tr>
        <td>UK</td>
        <td>VOD.L</td>
    </tr>
    <tr>
        <td>Japan</td>
        <td>7203.T</td>
    </tr>
    <tr>
        <td>Germany</td>
        <td>BMW.DE</td>
    </tr>
    <tr>
        <td>Canada</td>
        <td>SHOP.TO</td>
    </tr>
</table>

<p>General Rule:</p>
<pre>&lt;SYMBOL&gt;.&lt;EXCHANGE_SUFFIX&gt;</pre>

<hr>

<h2>Example Response</h2>
<pre>{
  "symbol": "AAPL",
  "price": 189.22,
  "open": 187.4,
  "high": 190.1,
  "low": 186.9,
  "previous_close": 188.0,
  "market_cap": 2950000000000,
  "currency": "USD"
}</pre>

<hr>

<h2>Limitations</h2>
<ul>
    <li>Data may be delayed by a few minutes</li>
    <li>Not suitable for high-frequency trading bots</li>
    <li>Yahoo Finance is unofficial and may change fields occasionally</li>
</ul>

<p>Best suited for:</p>
<ul>
    <li>Dashboards</li>
    <li>Portfolio trackers</li>
    <li>Alerts</li>
    <li>Learning FastAPI</li>
</ul>

<hr>

<h2>Possible Enhancements</h2>
<ul>
    <li>Redis caching</li>
    <li>Historical price endpoint</li>
    <li>Multiple stocks in one request</li>
    <li>Email/SMS price alerts</li>
    <li>PostgreSQL storage</li>
    <li>JWT authentication</li>
    <li>React frontend</li>
    <li>Deployment on Render / Railway / VPS</li>
</ul>

<hr>

<h2>License</h2>
<p>Free to use for learning and personal projects.</p>

</div>

</body>
</html>
