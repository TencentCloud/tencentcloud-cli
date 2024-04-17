**Example 1: 获取实例运行日志**

获取实例运行日志

Input: 

```
tccli wedata DescribeInstanceLog --cli-unfold-argument  \
    --TaskId 20220408130054538 \
    --CurRunDate 2022-04-10 19:38:37 \
    --BrokerIp 172.168.0.1 \
    --OriginFileName ins-1
```

Output: 
```
{
    "Response": {
        "Data": "true",
        "InstanceLogInfo": {
            "LogInfo": "日志记录"
        },
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

