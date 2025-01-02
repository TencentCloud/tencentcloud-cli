**Example 1: 查询函数下的全部别名**



Input: 

```
tccli scf ListAliases --cli-unfold-argument  \
    --Namespace default \
    --FunctionName functionName1
```

Output: 
```
{
    "Response": {
        "Aliases": [
            {
                "ModTime": "2023-07-12 10:53:52",
                "AddTime": "2023-07-12 10:53:52",
                "Name": "$DEFAULT",
                "Description": "",
                "FunctionVersion": "$LATEST",
                "RoutingConfig": {
                    "AdditionalVersionWeights": [],
                    "AddtionVersionMatchs": []
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "dfdfdfd-e3ca-4756-bc18-09a22ec9048f"
    }
}
```

