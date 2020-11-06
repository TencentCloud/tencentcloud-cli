**Example 1: 获取环境列表**



Input: 

```
tccli tdmq DescribeEnvironments --cli-unfold-argument  \
    --EnvironmentId default \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "EnvironmentSet": [
            {
                "EnvironmentId": "default",
                "MsgTTL": 0,
                "Remark": "",
                "CreateTime": "2020-06-15 17:12:49",
                "UpdateTime": "2020-06-16 10:25:19"
            }
        ],
        "RequestId": "2235829c-2c9d-44b0-bce4-0ce0a147cce0"
    }
}
```

