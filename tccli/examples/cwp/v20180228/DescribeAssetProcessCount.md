**Example 1: 获取所有进程数量**



Input: 

```
tccli cwp DescribeAssetProcessCount --cli-unfold-argument  \
    --Name host1
```

Output: 
```
{
    "Response": {
        "Process": [
            {
                "Key": "key1",
                "Value": 10,
                "Desc": "desc of key1",
                "NewCount": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

