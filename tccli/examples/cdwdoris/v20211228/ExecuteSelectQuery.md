**Example 1: 根据sql查询**



Input: 

```
tccli cdwdoris ExecuteSelectQuery --cli-unfold-argument  \
    --Database abc \
    --Query abc \
    --PageNum 1 \
    --PageSize 1 \
    --UserName abc \
    --PassWord abc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Fields": [
            "abc"
        ],
        "FieldTypes": [
            "abc"
        ],
        "Rows": [
            {
                "DataRow": [
                    "abc"
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

