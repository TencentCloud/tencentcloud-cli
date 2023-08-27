**Example 1: 查询实例参数**

查询实例参数

Input: 

```
tccli cynosdb DescribeInstanceParams --cli-unfold-argument  \
    --ClusterId cynosdbmysql-ge5ck0jr \
    --ParamKeyword cdb \
    --InstanceIds cynosdbmysql-ins-kzavkukw
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "InstanceId": "cynosdbmysql-ins-1111111",
                "ParamsItems": [
                    {
                        "CurrentValue": "1",
                        "Default": "1",
                        "Description": "Controls the interval between successive column values.",
                        "EnumValue": [],
                        "Func": "",
                        "IsFunc": false,
                        "IsGlobal": 1,
                        "Max": "65535",
                        "Min": "1",
                        "NeedReboot": 0,
                        "ParamName": "auto_increment_increment",
                        "ParamType": "integer"
                    }
                ]
            }
        ],
        "RequestId": "12fc29c0-6a35-11ed-bc4c-d5b8675844ad"
    }
}
```

