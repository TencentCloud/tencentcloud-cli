**Example 1: 查看备份日志备份天数**



Input: 

```
tccli dcdb DescribeLogFileRetentionPeriod --cli-unfold-argument  \
    --InstanceId dcdbt-ak4b3m9l
```

Output: 
```
{
    "Response": {
        "Days": 30,
        "InstanceId": "dcdbt-ak4b3m9l",
        "RequestId": "a6e96bd9-ec89-4c02-9738-d33e783a4bae"
    }
}
```

