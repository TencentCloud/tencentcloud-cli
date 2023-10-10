**Example 1: 获取所有Web服务数量**



Input: 

```
tccli cwp DescribeAssetWebServiceCount --cli-unfold-argument  \
    --Name xx
```

Output: 
```
{
    "Response": {
        "WebServices": [
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

