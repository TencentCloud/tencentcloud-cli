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
                "ConfValue": "xx",
                "ConfKey": "xx",
                "ModifyRuleValue": "xx",
                "DefaultValue": "xx",
                "Editable": false,
                "NeedRestart": false,
                "FileName": "xxx",
                "ConfDesc": "xxx",
                "ModifyRuleType": "xx"
            },
            {
                "ConfValue": "xx",
                "ConfKey": "xx",
                "Editable": false,
                "DefaultValue": "xx",
                "ModifyRuleValue": "xx",
                "NeedRestart": false,
                "FileName": "xx",
                "ConfDesc": "xx",
                "ModifyRuleType": "xx"
            },
            {
                "ConfValue": "xx",
                "ConfKey": "xx",
                "Editable": false,
                "DefaultValue": "xx",
                "ModifyRuleValue": "xx",
                "NeedRestart": false,
                "FileName": "xx",
                "ConfDesc": "xx",
                "ModifyRuleType": "xx"
            },
            {
                "ConfValue": "xx",
                "ConfKey": "xx",
                "Editable": false,
                "DefaultValue": "xx",
                "ModifyRuleValue": "xx",
                "NeedRestart": false,
                "FileName": "xx",
                "ConfDesc": "xx",
                "ModifyRuleType": "xx"
            },
            {
                "ConfValue": "xx",
                "ConfKey": "xx",
                "Editable": false,
                "DefaultValue": "xx",
                "ModifyRuleValue": "xx",
                "NeedRestart": false,
                "FileName": "xx",
                "ConfDesc": "xx",
                "ModifyRuleType": "xx"
            },
            {
                "ConfValue": "xx",
                "ConfKey": "xx",
                "Editable": false,
                "DefaultValue": "xx",
                "ModifyRuleValue": "xx",
                "NeedRestart": false,
                "FileName": "xx",
                "ConfDesc": "xx",
                "ModifyRuleType": "xx"
            },
            {
                "ConfValue": "xx",
                "ConfKey": "xx",
                "Editable": false,
                "DefaultValue": "xx",
                "ModifyRuleValue": "xx",
                "NeedRestart": false,
                "FileName": "xx",
                "ConfDesc": "xx",
                "ModifyRuleType": "xx"
            },
            {
                "ConfValue": "xx",
                "ConfKey": "xx",
                "Editable": false,
                "DefaultValue": "xx",
                "ModifyRuleValue": "xx",
                "NeedRestart": false,
                "FileName": "xx",
                "ConfDesc": "xx",
                "ModifyRuleType": "xx"
            },
            {
                "ConfValue": "xx",
                "ConfKey": "xx",
                "Editable": false,
                "DefaultValue": "xx",
                "ModifyRuleValue": "xx",
                "NeedRestart": false,
                "FileName": "xx",
                "ConfDesc": "xx",
                "ModifyRuleType": "xx"
            },
            {
                "ConfValue": "xx",
                "ConfKey": "xx",
                "Editable": false,
                "DefaultValue": "xx",
                "ModifyRuleValue": "xx",
                "NeedRestart": false,
                "FileName": "xx",
                "ConfDesc": "xx",
                "ModifyRuleType": "xx"
            },
            {
                "ConfValue": "xx",
                "ConfKey": "xx",
                "Editable": false,
                "DefaultValue": "xx",
                "ModifyRuleValue": "xx",
                "NeedRestart": false,
                "FileName": "xx",
                "ConfDesc": "xx",
                "ModifyRuleType": "xx"
            }
        ],
        "UnConfigItems": [],
        "MapConfigItems": [],
        "ErrorMsg": "",
        "RequestId": "xx"
    }
}
```

