**Example 1: 获取主机所有资源数量**



Input: 

```
tccli cwp DescribeAssetHostTotalCount --cli-unfold-argument  \
    --Uuid xx \
    --Quuid xx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "Types": [
            {
                "Value": 0,
                "Key": "xx",
                "Desc": "xx"
            }
        ]
    }
}
```

