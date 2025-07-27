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
                "Name": "lower_case_table_names",
                "ParamType": "integer",
                "Default": "0",
                "Description": "If set to 0, table names are stored as specified and comparisons are case sensitive. If set to 1, they are stored in lowercase on disk and comparisons are not case sensitive.",
                "CurrentValue": "0",
                "NeedReboot": 1,
                "Max": 1,
                "Min": 0,
                "EnumValue": [],
                "MaxFunc": "64",
                "MinFunc": "1",
                "IsNotSupportEdit": true
            }
        ],
        "RequestId": "92131c95-aa65-44db-8c3c-e8cd67883b58"
    }
}
```

