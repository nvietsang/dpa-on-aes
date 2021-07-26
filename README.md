# Overview
This work performs a Differential Power Analysis (DPA) attack on AES-128. The target function is Sbox at the last round. Get each bit of the intermediate value and split the traces into 2 sets based on the value of that bit.

Note that choosing the first bit of intermediate value does not give the correct key.

Then we also implement a Correlation Power Analysis (CPA) attack and obtain the correct key. We did experiment with both Hamming Weight and Hamming Distance on the intermediate values.

# Author
- Viet-Sang Nguyen

# Usage
To compute the average trace of N = 2000 traces:
```
python3 avg_trace.py
```

To run DPA attack:
```
python3 main_dpa.py
```

To run CPA attack:
```
python3 main_cpa.py
```
