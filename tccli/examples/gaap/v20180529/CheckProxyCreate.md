**Example 1: 查询通道是否可以创建**



Input: 

```
tccli gaap CheckProxyCreate --cli-unfold-argument  \
    --AccessRegion SouthChina \
    --RealServerRegion EastChina \
    --Bandwidth 2 \
    --Concurrent 10
```

Output: 
```
{
    "Response": {
        "CheckFlag": 1,
        "RequestId": "50cfe60e-2cc8-4ff7-ba08-03769ea7259a"
    }
}
```

