**Example 1: 查询通道是否可以创建**



Input: 

```
tccli gaap CheckProxyCreate --cli-unfold-argument  \
    --Concurrent 2 \
    --Bandwidth 10 \
    --RealServerRegion SouthChina \
    --AccessRegion EastChina
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

