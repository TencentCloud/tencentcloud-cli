**Example 1: 获取参数列表**

在集群详情页面获取所有参数列表

Input: 

```
tccli cdwch DescribeInstanceKeyValConfigs --cli-unfold-argument  \
    --InstanceId cdwch-xxxx
```

Output: 
```
{
    "Response": {
        "ConfigItems": [
            {
                "ConfKey": "max_connections",
                "ConfValue": "4096",
                "DefaultValue": "4096",
                "NeedRestart": false,
                "Editable": true,
                "ConfDesc": "The maximum number of inbound connections.",
                "FileName": "config.xml",
                "ModifyRuleType": "",
                "ModifyRuleValue": "{\"ruleName\":\"int_maxmin\", \"max\": 262145, \"min\":4096 }",
                "Uin": "836178961123",
                "ModifyTime": "2025-01-25 12:00:00"
            }
        ],
        "UnConfigItems": [
            {
                "ConfKey": "max_table_size_to_drop",
                "ConfValue": "",
                "DefaultValue": "50000000000",
                "NeedRestart": false,
                "Editable": true,
                "ConfDesc": "",
                "FileName": "config.xml",
                "ModifyRuleType": "number",
                "ModifyRuleValue": "{\"ruleName\":\"int_bigthan\", \"min\":0 }",
                "Uin": "100000000000",
                "ModifyTime": ""
            }
        ],
        "MapConfigItems": [
            {
                "ConfKey": "logger",
                "Items": [
                    {
                        "ConfKey": "logger.level",
                        "ConfValue": "trace",
                        "DefaultValue": "",
                        "NeedRestart": false,
                        "Editable": false,
                        "ConfDesc": "",
                        "FileName": "",
                        "ModifyRuleType": "",
                        "ModifyRuleValue": "",
                        "Uin": "100000000000",
                        "ModifyTime": ""
                    }
                ]
            }
        ],
        "ErrorMsg": "",
        "RequestId": "6d00d832-cb73-4fb9-8216-aca54f040xxx"
    }
}
```

