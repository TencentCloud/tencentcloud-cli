**Example 1: 查询弹性网卡配额Internal**



Input: 

```
tccli vpc DescribeEniLimitInternal --cli-unfold-argument  \
    --InstanceId default ins-1ksiqu38 \
    --Owner 2323232 \
    --InstanceFamily S6 S1
```

Output: 
```
{
    "Response": {
        "EniLimitSet": [
            {
                "LowerMem": 0,
                "Val": 8,
                "InstanceFamily": "D1",
                "InstanceId": "default",
                "UpperCpu": 1000000,
                "LowerCpu": 16,
                "EniLimitId": 326,
                "UpperMem": 1000000,
                "Owner": "default",
                "Type": 0,
                "CreateTime": "2020-09-22 17:29:55"
            }
        ],
        "RequestId": "1b2534de-3f38-4913-921a-af5ff1a9cb73"
    }
}
```

