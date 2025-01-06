**Example 1: 查询函数版本**



Input: 

```
tccli scf ListVersionByFunction --cli-unfold-argument  \
    --FunctionName functionName1
```

Output: 
```
{
    "Response": {
        "Versions": [
            {
                "Version": "$LATEST",
                "Description": "",
                "AddTime": "2024-12-18 10:11:51",
                "ModTime": "2024-12-18 17:04:41",
                "Status": "Active"
            }
        ],
        "FunctionVersion": [
            "$LATEST"
        ],
        "TotalCount": 1,
        "RequestId": "sdssd-a36d-42d3-9c24-c276409592a7"
    }
}
```

