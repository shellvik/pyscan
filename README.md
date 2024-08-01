<h4 align="center"> Basic port scanner built in Python for fun.</h4>

<p align="center">
  <a href="https://github.com/shellvik/pyscan">
    <img src="https://github.com/shellvik/pyscan/src/pyscan.png">
  </a>
</p>

<p align="center"><img src="/src/pyscan.png" alt="Pyscan Demo"></p>

## Usage:
Pyscan takes one argument - IP or hostname:

```
python3 pyscan.py example.com
```
## Output:
You  can save output in a text file with tee:

```
pytho3 pyscan.py example.com | tee -a scanresult.txt
```
> Note: This is my initial attempt to make a port scanner, I'll add more features and optimize it as I learn new concepts.

