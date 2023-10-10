**Example 1: 获取所有Web站点数量**



Input: 

```
tccli cwp DescribeAssetWebLocationCount --cli-unfold-argument  \
    --Name xx
```

Output: 
```
{
    "Response": {
        "WebLocations": [
            {
                "Value": 0,
                "Key": "xx",
                "Desc": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

