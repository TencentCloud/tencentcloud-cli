**Example 1: xc**



Input: 

```
tccli rum DescribeRumLogExports --cli-unfold-argument  \
    --PageNum 1 \
    --ID 234763 \
    --PageSize 999
```

Output: 
```
{
    "Response": {
        "RequestId": "01a45bad-d053-4af8-9f60-0c4293574f5d",
        "Result": "{\"code\":0,\"data\":{\"page\":1,\"pageSize\":999,\"totalCount\":1,\"totalPage\":1,\"data\":[{\"id\":234763,\"name\":\"124858_log\",\"status\":\"\",\"message\":\"任务创建成功\",\"progress\":0,\"url\":\"\",\"updateUser\":\"TICLI\",\"updateTime\":\"2025-01-19 10:13:04\",\"type\":\"json\",\"createUser\":\"TICLI\",\"createTime\":\"2025-01-19 10:13:04\"}]},\"msg\":\"\"}"
    }
}
```

**Example 2: 获取日志列表**



Input: 

```
tccli rum DescribeRumLogExports --cli-unfold-argument  \
    --PageSize 999 \
    --ID 10 \
    --PageNum 1
```

Output: 
```
{
    "Response": {
        "Result": "{\"code\":0,\"data\":{\"page\":1,\"pageSize\":999,\"totalCount\":1,\"totalPage\":1,\"data\":[{\"id\":10,\"name\":\"10_log\",\"status\":\"\",\"message\":\"任务创建成功\",\"progress\":0,\"url\":\"\",\"updateUser\":\"TICLI\",\"updateTime\":\"2025-01-19 10:14:04\",\"type\":\"json\",\"createUser\":\"TICLI\",\"createTime\":\"2025-01-19 10:14:04\"}]},\"msg\":\"\"}",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

