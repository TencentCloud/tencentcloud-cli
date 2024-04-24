**Example 1: 查询维度数据**

根据维度列名和过滤条件，查询维度值

Input: 

```
tccli apm DescribeTagValues --cli-unfold-argument  \
    --Filters.0.Key service.instance \
    --Filters.0.Type = \
    --Filters.0.Value 127.0.0.1 \
    --TagKey servier.name
```

Output: 
```
{
    "Response": {
        "RequestId": "apz12zicapy-eqixuc-uehq346v59c62",
        "Values": [
            "sso-api",
            "auth-api"
        ]
    }
}
```

