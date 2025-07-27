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
            "ClsRegion": "ap-guangzhou",
            "Status": "ON",
            "LogSetId": "8dff8d62-fa10-4d6c-bee0-6e31a0ade975",
            "LogTopicId": "09c3c2d1-ac46-4e4e-b688-b73950e64682"
        },
        "SlowLog": {
            "ClsRegion": "ap-guangzhou",
            "Status": "OFF",
            "LogSetId": "8dff8d62-fa10-4d6c-bee0-6e31a0ade976",
            "LogTopicId": "09c3c2d1-ac46-4e4e-b688-b73950e64681"
        },
        "RequestId": "8a96c7fec3c747adb83cb0868c0107d5"
    }
}
```

