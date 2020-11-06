**Example 1: Querying whether the connection can be created**



Input: 

```
tccli gaap CheckProxyCreate --cli-unfold-argument  \
    --AccessRegion EastChina \
    --RealServerRegion SouthChina \
    --Bandwidth 10 \
    --Concurrent 2
```

Output: 
```
{
    "Response": {
        "CheckFlag": 1,
        "RequestId": "5c680029-66b2-4be8-9630-7bd316ce70dd"
    }
}
```

