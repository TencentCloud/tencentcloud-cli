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
                "ConfKey": "abc",
                "ConfValue": "abc",
                "DefaultValue": "abc",
                "NeedRestart": true,
                "Editable": true,
                "ConfDesc": "abc",
                "FileName": "abc",
                "ModifyRuleType": "abc",
                "ModifyRuleValue": "abc",
                "Uin": "abc",
                "ModifyTime": "abc"
            }
        ],
        "UnConfigItems": [
            {
                "ConfKey": "abc",
                "ConfValue": "abc",
                "DefaultValue": "abc",
                "NeedRestart": true,
                "Editable": true,
                "ConfDesc": "abc",
                "FileName": "abc",
                "ModifyRuleType": "abc",
                "ModifyRuleValue": "abc",
                "Uin": "abc",
                "ModifyTime": "abc"
            }
        ],
        "MapConfigItems": [
            {
                "ConfKey": "abc",
                "Items": [
                    {
                        "ConfKey": "abc",
                        "ConfValue": "abc",
                        "DefaultValue": "abc",
                        "NeedRestart": true,
                        "Editable": true,
                        "ConfDesc": "abc",
                        "FileName": "abc",
                        "ModifyRuleType": "abc",
                        "ModifyRuleValue": "abc",
                        "Uin": "abc",
                        "ModifyTime": "abc"
                    }
                ]
            }
        ],
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

