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
        "TemplateId": 2333,
        "Name": "andy",
        "EngineVersion": "5.7",
        "TotalCount": 72,
        "Items": [
            {
                "Name": "andy1",
                "ParamType": "intege",
                "Default": "1",
                "Description": "Determines the starting point for the AUTO_INCREMENT column value.",
                "CurrentValue": "1",
                "NeedReboot": 0,
                "Max": 65535,
                "Min": 0,
                "EnumValue": [
                    ""
                ],
                "MaxFunc": "10000",
                "MinFunc": "1",
                "IsNotSupportEdit": true
            }
        ],
        "Description": "The maximum permitted number of simultaneous client connections.",
        "TemplateType": "HIGH_STABILITY",
        "EngineType": "InnoDB",
        "RequestId": "92131c95-aa65-44db-8c3c-e8cd67883b58"
    }
}
```

