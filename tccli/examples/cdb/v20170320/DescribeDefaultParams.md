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
        "TotalCount": 0,
        "Items": [
            {
                "Name": "character_set_server",
                "ParamType": "enum",
                "Default": "{MIN(DBInitMemory/4+500,1000000)}",
                "Description": "The maximum permitted number of simultaneous client connections.",
                "CurrentValue": "1600",
                "NeedReboot": 0,
                "Max": 0,
                "Min": 0,
                "EnumValue": [
                    "LATIN1",
                    "UTF8",
                    "GBK",
                    "UTF8MB4"
                ],
                "MaxFunc": "64",
                "MinFunc": "1",
                "IsNotSupportEdit": true
            }
        ],
        "RequestId": "92131c95-aa65-44db-8c3c-e8cd67883b58"
    }
}
```

