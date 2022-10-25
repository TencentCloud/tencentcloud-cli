**Example 1: 查询安全日志投递kafka配置**



Input: 

```
tccli tcss DescribeSecLogDeliveryKafkaSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceID": "实例ID",
        "InstanceName": "实例名称",
        "Domain": "域名",
        "LogTypeList": [
            {
                "LogType": "container_bash",
                "TopicID": "主题ID",
                "TopicName": "主题名称",
                "State": true
            }
        ],
        "User": "test",
        "RegionID": "xxx",
        "RequestId": "29b37d86-f63d-43d1-b21a-640e82965198"
    }
}
```

