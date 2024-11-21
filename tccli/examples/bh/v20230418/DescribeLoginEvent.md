**Example 1: 查询登录日志列表**



Input: 

```
tccli bh DescribeLoginEvent --cli-unfold-argument  \
    --UserName zhangsan
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "LoginEventSet": [
            {
                "UserName": "zhangsan",
                "RealName": "张三",
                "Result": 1,
                "Time": "2020-09-22T00:00:00+00:00",
                "Entry": 1,
                "SourceIp": "127.0.0.1"
            }
        ],
        "RequestId": "b8ebf0b3-ecf5-49bf-9f9d-86341c4072f1"
    }
}
```

