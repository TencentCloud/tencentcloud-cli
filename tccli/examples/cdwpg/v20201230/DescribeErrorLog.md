**Example 1: 错误日志**

查询错误日志详细信息

Input: 

```
tccli cdwpg DescribeErrorLog --cli-unfold-argument  \
    --InstanceId cdwpg-xx \
    --StartTime 2012-12-12 12:12:12 \
    --EndTime 2012-12-13 12:12:12 \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RequestId": "sxx",
        "ErrorLogDetails": [
            {
                "UserName": "cran",
                "ErrorMessage": "xdx",
                "ErrorTime": "2012-12-12 12:12:12",
                "Database": "test"
            }
        ]
    }
}
```

