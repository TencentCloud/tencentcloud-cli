**Example 1: 查询表**



Input: 

```
tccli cdwdoris QueryTableData --cli-unfold-argument  \
    --Database abc \
    --Table abc \
    --SelectedFields abc \
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

