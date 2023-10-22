**Example 1: 查询实例日志投递CLS配置**

实例日志管理中，慢日志、错误日志投递CLS的配置

Input: 

```
tccli cdb DescribeDBInstanceLogToCLS --cli-unfold-argument  \
    --InstanceId cdb-70zdmgg1
```

Output: 
```
{
    "Response": {
        "ErrorLog": {
            "Status": "ON",
            "LogSetId": "test",
            "LogTopicId": "test"
        },
        "SlowLog": {
            "Status": "OFF",
            "LogSetId": "test",
            "LogTopicId": "test"
        },
        "RequestId": "8a96c7fec3c747adb83cb0868c0107d5"
    }
}
```

