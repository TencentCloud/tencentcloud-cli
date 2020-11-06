**Example 1: 查看备份日志备份天数**



Input: 

```
tccli mariadb DescribeLogFileRetentionPeriod --cli-unfold-argument  \
    --InstanceId tdsql-ige1a5k3
```

Output: 
```
{
    "Response": {
        "InstanceId": "tdsql-ige1a5k3",
        "Days": 30,
        "RequestId": "87e86e78-340f-48f3-a84b-a42517d7aa46"
    }
}
```

