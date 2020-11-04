**Example 1: 查询函数版本**



Input: 

```
tccli scf ListVersionByFunction --cli-unfold-argument  \
    --FunctionName xxxxx
```

Output: 
```
{
    "Response": {
        "FunctionVersion": [
            "$LATEST",
            "3",
            "2",
            "1"
        ],
        "RequestId": "d1b93f9c-ac3a-412a-a4f3-6f0697099f72",
        "Versions": [
            {
                "Version": "$LATEST",
                "Description": "123"
            },
            {
                "Version": "3",
                "Description": "123"
            },
            {
                "Version": "2",
                "Description": "123"
            },
            {
                "Version": "1",
                "Description": "123"
            }
        ]
    }
}
```

