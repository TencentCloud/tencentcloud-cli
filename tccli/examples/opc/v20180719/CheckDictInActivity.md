**Example 1: 批量查询**

批量查询dictid是否在某个活动中

Input: 

```
tccli opc CheckDictInActivity --cli-unfold-argument  \
    --DictIds 2011 2321 2000
```

Output: 
```
{
    "Response": {
        "RequestId": "78c6a62e-e0c1-474f-802d-42a341e24c8b",
        "Result": [
            {
                "DictId": 2000,
                "Result": false
            },
            {
                "DictId": 2321,
                "Result": false
            },
            {
                "DictId": 2011,
                "Result": false
            }
        ]
    }
}
```

