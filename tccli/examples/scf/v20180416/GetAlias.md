**Example 1: 查询别名详细信息**



Input: 

```
tccli scf GetAlias --cli-unfold-argument  \
    --Namespace <Namespace>\
    --FunctionName <FunctionName>\
    --Name <AliasName>
```

Output: 
```
{
    "Response": {
        "RequestId": "d1b93f9c-ac3a-412a-a4f3-6f0697099f72",
        "FunctionVersion": "1",
        "Name": "al3",
        "RoutingConfig": {
            "AdditionalVersionWeights": [
                {
                    "Version": "3",
                    "Weight": 0.3
                },
                {
                    "Version": "2",
                    "Weight": 0.2
                }
            ]
        },
        "Description": ""
    }
}
```

