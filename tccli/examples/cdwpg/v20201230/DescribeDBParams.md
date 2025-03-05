**Example 1: 1**



Input: 

```
tccli cdwpg DescribeDBParams --cli-unfold-argument  \
    --InstanceId cdwpg-xx \
    --Limit 20 \
    --NodeTypes dn \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xxss",
        "Items": [
            {
                "NodeType": "cn",
                "NodeName": "cn001",
                "TotalCount": 2,
                "Details": [
                    {
                        "ParamName": "MaxConnections",
                        "DefaultValue": "100",
                        "NeedRestart": false,
                        "RunningValue": "100",
                        "ValueRange": {
                            "Type": "enum",
                            "Enum": [
                                "DEBUG",
                                "INFO",
                                "WARN",
                                "ERROR"
                            ],
                            "Range": {
                                "Min": "1024",
                                "Max": "4096"
                            },
                            "String": ""
                        },
                        "Unit": "connections",
                        "ShortDesc": "Maximum number of concurrent connections",
                        "ParameterName": "cds"
                    }
                ]
            }
        ]
    }
}
```

