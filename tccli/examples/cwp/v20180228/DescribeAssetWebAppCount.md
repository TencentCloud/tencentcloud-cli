**Example 1: 获取所有Web应用数量**



Input: 

```
tccli cwp DescribeAssetWebAppCount --cli-unfold-argument  \
    --Name xx
```

Output: 
```
{
    "Response": {
        "WebApps": [
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

