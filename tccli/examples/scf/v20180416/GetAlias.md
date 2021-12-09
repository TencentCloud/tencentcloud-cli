**Example 1: 查询别名详细信息**



Input: 

```
tccli scf GetAlias --cli-unfold-argument  \
    --Namespace <Namespace> \
    --FunctionName <FunctionName> \
    --Name <AliasName>
```

Output: 
```
{
    "Response": {
        "ModTime": "2020-09-22 00:00:00",
        "Description": "xx",
        "AddTime": "2020-09-22 00:00:00",
        "FunctionVersion": "xx",
        "RequestId": "xx",
        "RoutingConfig": {
            "AdditionalVersionWeights": [
                {
                    "Version": "xx",
                    "Weight": 0.3
                },
                {
                    "Version": "xx",
                    "Weight": 0.2
                }
            ],
            "AddtionVersionMatchs": [
                {
                    "Version": "xx",
                    "Expression": "xx",
                    "Method": "xx",
                    "Key": "xx"
                }
            ]
        },
        "Name": "xx"
    }
}
```

