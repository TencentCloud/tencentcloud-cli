**Example 1: 获取Kafka导入配置信息**

获取Kafka导入配置信息

Input: 

```
tccli cls DescribeKafkaRecharges --cli-unfold-argument  \
    --TopicId abc \
    --Status 1
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Id": "abc",
                "TopicId": "abc",
                "Name": "abc",
                "ServerAddr": "test.cls.tencentyun.com:9095",
                "UserKafkaTopics": "topic1,topic2",
                "ConsumerGroupName": "",
                "Status": 1,
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "LogRechargeRule": {
                    "RechargeType": "json_log",
                    "TimeKey": "abc",
                    "TimeFormat": "abc",
                    "LogRegex": "abc",
                    "UnMatchLogSwitch": true,
                    "UnMatchLogKey": "abc",
                    "EncodingFormat": 0,
                    "DefaultTimeSwitch": true
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

