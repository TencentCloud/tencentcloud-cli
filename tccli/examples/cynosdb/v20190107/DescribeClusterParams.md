**Example 1: 查询集群参数**

查询集群参数

Input: 

```
tccli cynosdb DescribeClusterParams --cli-unfold-argument  \
    --ClusterId cynosdbpg-1xcycbu8
```

Output: 
```
{
    "Response": {
        "TotalCount": 226,
        "Items": [
            {
                "CurrentValue": "1000",
                "Default": "60000",
                "EnumValue": [
                    "OFF",
                    "ON"
                ],
                "Max": "65535",
                "Min": "1",
                "ParamName": "auto_increment_increment",
                "NeedReboot": 0,
                "ParamType": "integer",
                "MatchType": "",
                "MatchValue": "",
                "Description": "Determines the starting point for the AUTO_INCREMENT column value.",
                "IsGlobal": 1,
                "ModifiableInfo": {
                    "IsModifiable": 1
                },
                "IsFunc": true,
                "Func": "{MIN(DBInitMemory/%d*%d,%d)},4000,32768,2097152"
            }
        ],
        "RequestId": "806fe1c8-5567-4aa8-a521-ea2414c793b4"
    }
}
```

