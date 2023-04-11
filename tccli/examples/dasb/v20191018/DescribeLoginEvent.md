**Example 1: 查询登录日志列表**



Input: 

```
tccli dasb DescribeLoginEvent --cli-unfold-argument  \
    --UserName xxx
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoginEventSet": [
            {
                "UserName": "xx",
                "RealName": "xx",
                "Result": 1,
                "Time": "2020-09-22T00:00:00+00:00",
                "Entry": 1,
                "SourceIp": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

