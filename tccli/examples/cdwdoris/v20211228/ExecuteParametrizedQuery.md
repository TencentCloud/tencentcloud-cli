**Example 1: 带参数查询**



Input: 

```
tccli cdwdoris ExecuteParametrizedQuery --cli-unfold-argument  \
    --InstanceId cdwdoris-xxx \
    --Database abc \
    --Sql SELECT year, SUM(number) as num FROM xxx WHERE name = @name GROUP BY year ORDER BY year \
    --QueryParameter.0.PropertyKey name \
    --QueryParameter.0.PropertyValue William \
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

