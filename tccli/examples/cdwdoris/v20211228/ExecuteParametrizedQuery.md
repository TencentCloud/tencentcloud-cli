**Example 1: 带参数查询**



Input: 

```
tccli cdwdoris ExecuteParametrizedQuery --cli-unfold-argument  \
    --InstanceId cdwdoris-xx \
    --Database __internal_schema \
    --Sql SELECT `query_id`, `time`, `stmt` FROM `audit_log` where query_id = @query_id and time = @time; \
    --QueryParameter.0.PropertyKey query_id \
    --QueryParameter.0.PropertyValue 100115473d1f4d0d-9211c31e6b77ddaf \
    --QueryParameter.1.PropertyKey time \
    --QueryParameter.1.PropertyValue 2024-08-30 06:14:20.064
```

Output: 
```
{
    "Response": {
        "Fields": [
            "query_id",
            "time",
            "stmt"
        ],
        "Rows": [
            {
                "DataRow": [
                    "100115473d1f4d0d-9211c31e6b77ddaf",
                    "2024-08-30 06:14:20.064 +0800 CST",
                    " SHOW PROC  '/frontends'"
                ]
            }
        ],
        "RequestId": "xx-xx-x-xx-xx"
    }
}
```

