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
        "TotalCount": 0,
        "Items": [
            {
                "CurrentValue": "abc",
                "Default": "abc",
                "EnumValue": [
                    "abc"
                ],
                "Max": "abc",
                "Min": "abc",
                "ParamName": "abc",
                "NeedReboot": 0,
                "ParamType": "abc",
                "MatchType": "abc",
                "MatchValue": "abc",
                "Description": "abc",
                "IsGlobal": 0,
                "ModifiableInfo": {
                    "IsModifiable": 0
                },
                "IsFunc": true,
                "Func": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

