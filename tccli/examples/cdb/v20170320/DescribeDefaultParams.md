**Example 1: 查询默认的可设置参数列表**

查询默认的可设置参数列表

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
                "CurrentValue": "utf8",
                "Default": "LATIN1",
                "Description": "Specify default server character set",
                "EnumValue": [
                    "LATIN1",
                    "UTF8",
                    "GBK",
                    "UTF8MB4"
                ],
                "Max": 0,
                "MaxFunc": "",
                "Min": 0,
                "MinFunc": "",
                "Name": "character_set_server",
                "NeedReboot": 1,
                "ParamType": "enum"
            },
            {
                "CurrentValue": "1600",
                "Default": "{MIN(DBInitMemory/4+500,1000000)}",
                "Description": "The maximum permitted number of simultaneous client connections.",
                "EnumValue": [],
                "Max": 100000,
                "MaxFunc": "100000",
                "Min": 1,
                "MinFunc": "1",
                "Name": "max_connections",
                "NeedReboot": 0,
                "ParamType": "func"
            }
        ]
    }
}
```

