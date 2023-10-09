**Example 1: 获取所有账号数量**



Input: 

```
tccli cwp DescribeAssetUserCount --cli-unfold-argument  \
    --Name xx
```

Output: 
```
{
    "Response": {
        "Users": [
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

