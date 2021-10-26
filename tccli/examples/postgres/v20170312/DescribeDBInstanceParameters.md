**Example 1: 获取实例参数列表**

查看实例当前可修改该参数列表

Input: 

```
tccli postgres DescribeDBInstanceParameters --cli-unfold-argument  \
    --DBInstanceId xx \
    --ParamName default_transaction_read_only
```

Output: 
```
{
    "Response": {
        "Detail": [
            {
                "Advanced": true,
                "ClassificationCN": "Client Connection Defaults",
                "ClassificationEN": "Sets the default read-only status of new transactions.",
                "CurrentValue": "",
                "DefaultValue": "off",
                "EnumValue": [
                    "on",
                    "off"
                ],
                "ID": 59,
                "LastModifyTime": "",
                "Max": 0,
                "Min": 0,
                "Name": "default_transaction_read_only",
                "NeedReboot": false,
                "ParamDescriptionCH": "此参数控制每个新事务的是否为默认只读状态 。默认是off（读/写）",
                "ParamDescriptionEN": "Sets the default read-only status of new transactions.",
                "ParamValueType": "bool",
                "SpecRelated": false,
                "Unit": ""
            }
        ],
        "RequestId": "",
        "TotalCount": 1
    }
}
```

