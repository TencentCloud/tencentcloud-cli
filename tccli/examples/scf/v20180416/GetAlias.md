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
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Name": "ddd",
        "Description": "",
        "FunctionVersion": "1",
        "RoutingConfig": {
            "AdditionalVersionWeights": [
                {
                    "Version": "$LATEST",
                    "Weight": 0.8
                }
            ],
            "AddtionVersionMatchs": []
        },
        "AddTime": "2024-12-19 14:53:51",
        "ModTime": "2024-12-19 14:53:51"
    }
}
```

