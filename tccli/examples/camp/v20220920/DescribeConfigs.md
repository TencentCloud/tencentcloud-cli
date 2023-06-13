**Example 1: 查询配置**

查询配置

Input: 

```
tccli camp DescribeConfigs --cli-unfold-argument  \
    --Platform abc \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.Query abc \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Filters": [
            {
                "Name": "abc",
                "Values": [
                    "abc"
                ],
                "Query": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

