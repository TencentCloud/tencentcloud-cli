**Example 1: 获取实例运行日志**

获取实例运行日志

Input: 

```
tccli wedata DescribeInstanceLog --cli-unfold-argument  \
    --TaskId abc \
    --CurRunDate abc \
    --BrokerIp abc \
    --OriginFileName abc
```

Output: 
```
{
    "Response": {
        "Data": "abc",
        "InstanceLogInfo": {
            "LogInfo": "abc"
        },
        "RequestId": "abc"
    }
}
```

