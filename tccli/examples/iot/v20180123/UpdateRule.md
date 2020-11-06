**Example 1: 更新规则**

更新规则

Input: 

```
tccli iot UpdateRule --cli-unfold-argument  \
    --RuleId rule-osh3ckco \
    --Name 新规则名称 \
    --Description 新规则描述 \
    --Query.Field * \
    --Query.Topic iot-4e0wsxpi/+/new-topic-1 \
    --Query.Condition  \
    --Actions.0.Topic.Topic iot-gl9kmqrs/new-device-1/new-topic-1 \
    --Actions.1.Service.Url http://abc.com
```

Output: 
```
{
    "Response": {
        "RequestId": "07ae8cda-4ff1-4112-914e-32afca4fcffd",
        "Rule": {
            "RuleId": "rule-ox6djvws",
            "AppId": 1251006373,
            "Name": "aaa",
            "Description": "aaaaaa",
            "Query": {
                "Field": "字符串",
                "Topic": "iot-5aawn3i8/asdf/asdfa",
                "Condition": "1=1"
            },
            "Actions": [
                {
                    "Topic": {
                        "Topic": "iot-gl9kmqrs/new-device-1/new-topic-1"
                    },
                    "Service": null
                },
                {
                    "Service": {
                        "Url": "http://abc.com"
                    },
                    "Topic": null
                }
            ],
            "MsgOrder": 0,
            "DataType": 0,
            "Active": 0,
            "Deleted": 0,
            "CreateTime": "2018-06-26 13:15:18",
            "UpdateTime": "2018-07-04 14:45:40"
        }
    }
}
```

**Example 2: 更新规则转发CKafka**

更新规则转发CKafka

Input: 

```
tccli iot UpdateRule --cli-unfold-argument  \
    --RuleId rule-46d6lldw \
    --Query.Field * \
    --Query.ProductId iot-4e0wsxpi \
    --Query.Condition  \
    --Actions.0.Ckafka.Region gz \
    --Actions.0.Ckafka.InstanceId ckafka-fsl0f3wv \
    --Actions.0.Ckafka.TopicName shadow_events
```

Output: 
```
{
    "Response": {
        "RequestId": "246dcf82-4bb4-4957-9f1f-075afab5cd60",
        "Rule": {
            "RuleId": "rule-46d6lldw",
            "AppId": 1251006373,
            "Name": "字符串1",
            "Description": "字符串",
            "Query": {
                "Field": "*",
                "ProductId": "iot-4e0wsxpi",
                "Condition": "",
                "Topic": null
            },
            "Actions": [
                {
                    "Ckafka": {
                        "Region": "gz",
                        "InstanceId": "ckafka-fsl0f3wv",
                        "TopicName": "shadow_events"
                    },
                    "Topic": null,
                    "Service": null
                }
            ],
            "MsgOrder": 0,
            "DataType": 0,
            "Active": 0,
            "Deleted": 0,
            "CreateTime": "2018-07-06 11:37:18",
            "UpdateTime": "2018-07-11 23:00:20"
        }
    }
}
```

