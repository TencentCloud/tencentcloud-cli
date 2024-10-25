**Example 1: 查询函数下的全部别名**



Input: 

```
tccli scf ListAliases --cli-unfold-argument  \
    --Namespace <Namespace> \
    --FunctionName <FunctionName>
```

Output: 
```
{
    "Response": {
        "Aliases": [
            {
                "FunctionVersion": "abc",
                "Name": "abc",
                "RoutingConfig": {
                    "AdditionalVersionWeights": [
                        {
                            "Version": "abc",
                            "Weight": 0
                        }
                    ],
                    "AddtionVersionMatchs": [
                        {
                            "Version": "abc",
                            "Key": "abc",
                            "Method": "abc",
                            "Expression": "abc"
                        }
                    ]
                },
                "Description": "abc",
                "AddTime": "2020-09-22 00:00:00",
                "ModTime": "2020-09-22 00:00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

