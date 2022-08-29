**Example 1: 查询弹性网卡或者子机相关自定义配额**



Input: 

```
tccli vpc DescribeEniLimitDetailInternal --cli-unfold-argument  \
    --InstanceFamily S6 S1 \
    --InstanceId ins-1ksiqu38 \
    --Mem 8 \
    --Owner 2323232 \
    --Type 2 1 \
    --Cpu 4
```

Output: 
```
{
    "Response": {
        "EniLimitDetail": [
            {
                "LimitType": "0",
                "LimitValue": 2
            },
            {
                "LimitType": "1",
                "LimitValue": 6
            },
            {
                "LimitType": "2",
                "LimitValue": 0
            },
            {
                "LimitType": "3",
                "LimitValue": 0
            },
            {
                "LimitType": "4",
                "LimitValue": 100
            },
            {
                "LimitType": "5",
                "LimitValue": 8
            },
            {
                "LimitType": "27",
                "LimitValue": 0
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

