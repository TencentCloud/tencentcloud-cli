**Example 1: 查询实例的可设置参数列表**

查询实例的可设置参数列表

Input: 

```
tccli cdb DescribeInstanceParams --cli-unfold-argument  \
    --InstanceId cdb-ezq1vzem
```

Output: 
```
{
    "Response": {
        "TotalCount": 72,
        "Items": [
            {
                "Name": "max_connections",
                "ParamType": "integer",
                "Default": "151",
                "Description": "The maximum permitted number of simultaneous client connections.",
                "CurrentValue": "800",
                "NeedReboot": 0,
                "Max": 10240,
                "Min": 1,
                "EnumValue": [],
                "MinFunc": "",
                "MaxFunc": ""
            },
            {
                "Name": "character_set_server",
                "ParamType": "enum",
                "Default": "utf8",
                "Description": "Specify default server character set.",
                "CurrentValue": "utf8",
                "NeedReboot": 1,
                "EnumValue": [
                    "utf8",
                    "utf8mb4",
                    "gbk",
                    "latin1"
                ],
                "Max": 0,
                "Min": 0,
                "MinFunc": "",
                "MaxFunc": ""
            },
            {
                "Name": "lower_case_table_names",
                "ParamType": "integer",
                "Default": "0",
                "Description": "If set to 0, table names are stored as specified and comparisons are case sensitive. If set to 1, they are stored in lowercase on disk and comparisons are not case sensitive.",
                "CurrentValue": "0",
                "NeedReboot": 1,
                "Max": 1,
                "Min": 0,
                "EnumValue": [],
                "MinFunc": "",
                "MaxFunc": ""
            }
        ],
        "RequestId": "92131c95-aa65-44db-8c3c-e8cd67883b58"
    }
}
```

