**Example 1: 查询登录日志列表**



Input: 

```
tccli dasb DescribeLoginEvent --cli-unfold-argument  \
    --UserName Oliver \
    --RealName Henry \
    --StartTime 2020-09-22T00:00:00+08:00 \
    --EndTime 2020-09-22T00:00:00+08:00 \
    --SourceIp 127.41.14.47 \
    --Entry 1 \
    --Result 1 \
    --Offset 1 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoginEventSet": [
            {
                "UserName": "Henry",
                "RealName": "Oliver",
                "Result": 1,
                "Time": "2020-09-22T00:00:00+08:00",
                "Entry": 1,
                "SourceIp": "10.45.58.74"
            }
        ],
        "RequestId": "3bf47843-f8b2-40f7-8963-76d9506eed22"
    }
}
```

