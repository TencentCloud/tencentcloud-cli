**Example 1: 查询操作日志列表**



Input: 

```
tccli dasb DescribeOperationEvent --cli-unfold-argument  \
    --UserName xxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "OperationEventSet": [
            {
                "UserName": "xx",
                "Kind": 1,
                "RealName": "xx",
                "Result": 1,
                "Time": "2020-09-22T00:00:00+00:00",
                "Operation": "xx",
                "SourceIp": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

