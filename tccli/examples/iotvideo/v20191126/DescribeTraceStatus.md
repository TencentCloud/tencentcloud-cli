**Example 1: 查询指定设备是否在白名单**



Input: 

```
tccli iotvideo DescribeTraceStatus --cli-unfold-argument  \
    --Tids xxx0 xxx1
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Tid": "xxx0",
                "IsExist": true
            },
            {
                "Tid": "xxx1",
                "IsExist": false
            }
        ],
        "RequestId": "e4f37100-3afb-40ea-99c1-5cc5a8c6e953"
    }
}
```

