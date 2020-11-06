**Example 1: 获取转发规则列表**

获取转发规则列表

Input: 

```
tccli iot GetRules --cli-unfold-argument  \
    --Offset 0 \
    --Length 2
```

Output: 
```
{
    "Response": {
        "RequestId": "fcb69522-3602-479f-8a69-26e5ed564636",
        "Rules": [
            {
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
            },
            {
                "RuleId": "rule-amxh05xe",
                "AppId": 1251006373,
                "Name": "字符串",
                "Description": "字符串",
                "Query": {
                    "Field": "*",
                    "Topic": "iot-5aawn3i8/a/b",
                    "Condition": "1=1"
                },
                "Actions": [],
                "MsgOrder": 0,
                "DataType": 0,
                "Active": 0,
                "Deleted": 0,
                "CreateTime": "2018-06-26 13:11:11",
                "UpdateTime": "2018-06-26 13:11:11"
            }
        ],
        "Total": 2
    }
}
```

