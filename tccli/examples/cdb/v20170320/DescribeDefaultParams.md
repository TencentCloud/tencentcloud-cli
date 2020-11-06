**Example 1: Querying the list of default configurable parameters**



Input: 

```
tccli cdb DescribeDefaultParams --cli-unfold-argument  \
    --EngineVersion 5.7
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "RequestId": "92131c95-aa65-44db-8c3c-e8cd67883b58",
        "Items": [
            {
                "CurrentValue": "800",
                "Name": "max_connections",
                "Min": 1,
                "Default": "151",
                "Max": 10240,
                "ParamType": "integer",
                "EnumValue": [],
                "NeedReboot": 0,
                "Description": "The maximum permitted number of simultaneous client connections."
            },
            {
                "CurrentValue": "utf8",
                "Name": "character_set_server",
                "Min": 0,
                "Default": "utf8",
                "Max": 0,
                "ParamType": "enum",
                "EnumValue": [
                    "utf8",
                    "utf8mb4",
                    "gbk",
                    "latin1"
                ],
                "NeedReboot": 1,
                "Description": "Specify default server character set."
            }
        ]
    }
}
```

