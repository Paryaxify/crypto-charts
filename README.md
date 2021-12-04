<h1>Overview</h1>
Crypto chart analysis is <em>currently</em> a static chart analysis application made using static datasets using <strong>Dash</strong> which combines plotly.js and react.js to create a simpler framework for interactive graphs.<br>
This application consists of crypto prices till <em>July 2021</em>
<hr>
<h2>Setup</h2>
<h3>Linux</h3>
Setup on Linux can be done using 2 ways - <br>
<strong>1.Using make</strong><br>
<ul>
<li>Clone the repo in desired directory.</li>
<li>

```
$ make run
```
</li>
<li>The default port is <strong>8000</strong>. Dashboard can be accessed at
<strong>localhost:8000</strong>
</li>
</ul>
<strong>2. Manual installation</strong><br>
<ul>
<li>Clone the repo in desired directory.</li>
<strong>Optional : </strong>Create a python virtual environment<br>

```
$ python3 -m venv venv
$ source venv/bin/activate
```
<li>

```
pip install -r requirements.txt
```
</li>
<li>

```
python3 app.py
```
</li>
<li>The default port is <strong>8000</strong>. Dashboard can be accessed at
<strong>localhost:8000</strong>
</li>
</ul>

<h3>Windows</h3>
Haven't personally tested this in a Windows environment but manual installation steps are - 
<ul>
<li>Clone the repo in desired directory.</li>
<strong>Optional : </strong>Create a python virtual environment<br>

```
$ virtualenv venv
$ venv\Scripts\activate
```
<li>

```
pip install -r requirements.txt
```
<li>

```
python3 app.py
```
</li>
<li>The default port is <strong>8000</strong>. Dashboard can be accessed at
<strong>localhost:8000</strong>
</li>
</ul> 

