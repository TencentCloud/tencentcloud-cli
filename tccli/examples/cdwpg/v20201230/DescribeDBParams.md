**Example 1: 配置描述**



Input: 

```
tccli cdwpg DescribeDBParams --cli-unfold-argument  \
    --InstanceId cdwpg-xdsccxxx \
    --Limit 1 \
    --NodeTypes cn \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Details": [
                    {
                        "DefaultValue": "off",
                        "NeedRestart": false,
                        "ParamName": "enable_audit",
                        "ParameterName": "enable_audit",
                        "RunningValue": "off",
                        "ShortDesc": "Enable to audit user operations on the database objects.",
                        "Unit": "NULL",
                        "ValueRange": {
                            "Enum": [
                                ""
                            ],
                            "Range": {
                                "Max": "on",
                                "Min": "off"
                            },
                            "String": "",
                            "Type": "section"
                        }
                    }
                ],
                "NodeName": "cn0001",
                "NodeType": "cn",
                "TotalCount": 1
            },
            {
                "Details": [
                    {
                        "DefaultValue": "off",
                        "NeedRestart": false,
                        "ParamName": "enable_audit",
                        "ParameterName": "enable_audit",
                        "RunningValue": "off",
                        "ShortDesc": "Enable to audit user operations on the database objects.",
                        "Unit": "NULL",
                        "ValueRange": {
                            "Enum": [
                                ""
                            ],
                            "Range": {
                                "Max": "on",
                                "Min": "off"
                            },
                            "String": "",
                            "Type": "section"
                        }
                    }
                ],
                "NodeName": "cn0002",
                "NodeType": "cn",
                "TotalCount": 1
            }
        ],
        "RequestId": "c5855fc1-e653-4eb6-958c-556ee7942c4c",
        "TotalCount": 2
    }
}
```

