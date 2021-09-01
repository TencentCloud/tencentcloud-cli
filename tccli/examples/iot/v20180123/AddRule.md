**Example 1: 新增规则**

新增规则

Input: 

```
tccli iot AddRule --cli-unfold-argument  \
    --Name 规则名称 \
    --Description 规则描述 \
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

