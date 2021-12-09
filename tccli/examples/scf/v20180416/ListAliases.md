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
        "TotalCount": 1,
        "RequestId": "xx",
        "Aliases": [
            {
                "ModTime": "2020-09-22 00:00:00",
                "Name": "xx",
                "AddTime": "2020-09-22 00:00:00",
                "FunctionVersion": "xx",
                "RoutingConfig": {
                    "AdditionalVersionWeights": [
                        {
                            "Version": "xx",
                            "Weight": 0.0
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
                "Description": "xx"
            }
        ]
    }
}
```

