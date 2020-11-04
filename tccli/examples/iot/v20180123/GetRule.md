**Example 1: 获取转发规则信息**

获取转发规则信息

Input: 

```
tccli iot GetRule --cli-unfold-argument  \
    --RuleId rule-8tju9mg6
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

