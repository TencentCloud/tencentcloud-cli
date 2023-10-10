**Example 1: 获取所有软件应用数量**



Input: 

```
tccli cwp DescribeAssetAppCount --cli-unfold-argument  \
    --Name xx
```

Output: 
```
{
    "Response": {
        "Apps": [
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

