**Example 1: 查询参数模板详情**

该接口用于查询参数模板详细详情。

Input: 

```
tccli cdb DescribeParamTemplateInfo --cli-unfold-argument  \
    --TemplateId 233
```

Output: 
```
{
    "Response": {
        "TemplateId": 233,
        "Name": "test",
        "EngineVersion": "5.7",
        "Description": "test",
        "TotalCount": 72,
        "TemplateType": "HIGH_STABILITY",
        "RequestId": "92131c95-aa65-44db-8c3c-e8cd67883b58",
        "EngineType": "InnoDB",
        "Items": [
            {
                "CurrentValue": "1",
                "Default": "1",
                "Description": "Controls the interval between successive column values.",
                "EnumValue": [],
                "Max": 65535,
                "MaxFunc": "",
                "Min": 1,
                "MinFunc": "",
                "Name": "auto_increment_increment",
                "NeedReboot": 0,
                "ParamType": "integer"
            },
            {
                "CurrentValue": "1",
                "Default": "1",
                "Description": "Determines the starting point for the AUTO_INCREMENT column value.",
                "EnumValue": [],
                "Max": 65535,
                "MaxFunc": "",
                "Min": 1,
                "MinFunc": "",
                "Name": "auto_increment_offset",
                "NeedReboot": 0,
                "ParamType": "integer"
            },
            {
                "CurrentValue": "800",
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

