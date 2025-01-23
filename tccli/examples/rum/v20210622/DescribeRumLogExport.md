**Example 1: 1212**



Input: 

```
tccli rum DescribeRumLogExport --cli-unfold-argument  \
    --Query id:1 \
    --EndTime 1 \
    --Name  \
    --StartTime 1665994920000 \
    --ID 1
```

Output: 
```
{
    "Response": {
        "RequestId": "763188d1-9f99-45e8-8bbf-bcdffa8f58f0",
        "Result": "{\"code\":0,\"data\":{\"id\":1,\"name\":\"132445_log\",\"message\":\"\"},\"msg\":\"\"}"
    }
}
```

**Example 2: 获取日志列表**



Input: 

```
tccli rum DescribeRumLogExport --cli-unfold-argument  \
    --Name logDemo \
    --Fields date \
    --StartTime 1714103013 \
    --Query id:15 \
    --EndTime 1714103013 \
    --ID 15
```

Output: 
```
{
    "Response": {
        "Result": "{\"code\":0,\"data\":{\"id\":15,\"name\":\"132495_log\",\"message\":\"\"},\"msg\":\"\"}",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

