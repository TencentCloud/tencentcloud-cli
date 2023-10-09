**Example 1: 获取所有数据库数量**



Input: 

```
tccli cwp DescribeAssetDatabaseCount --cli-unfold-argument  \
    --Name xx
```

Output: 
```
{
    "Response": {
        "Databases": [
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

