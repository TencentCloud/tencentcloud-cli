**Example 1: 带参数查询**



Input: 

```
tccli cdwdoris ExecuteParametrizedQuery --cli-unfold-argument  \
    --Database abc \
    --Sql abc \
    --QueryParameter.0.PropertyKey abc \
    --QueryParameter.0.PropertyValue abc \
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

