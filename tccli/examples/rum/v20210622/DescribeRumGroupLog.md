**Example 1: 2312**



Input: 

```
tccli rum DescribeRumGroupLog --cli-unfold-argument  \
    --OrderBy asc \
    --ID 1 \
    --Limit 1 \
    --GroupField date \
    --StartTime 1 \
    --Query 1 \
    --EndTime 1 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "RequestId": "81a43a52-d00f-462a-82da-89841117f4ca",
        "Result": "{\"code\":0,\"data\":[{\"1737254300150\":1},{\"1737254310941\":1}],\"msg\":\"\",\"request_id\":\"81a43a52-d00f-462a-82da-89841117f4ca\"}"
    }
}
```

**Example 2: 获取日志列表**



Input: 

```
tccli rum DescribeRumGroupLog --cli-unfold-argument  \
    --OrderBy "desc" \
    --StartTime "1" \
    --Limit 10 \
    --Query "*" \
    --EndTime "20" \
    --ID 10 \
    --Page 1 \
    --GroupField date
```

Output: 
```
{
    "Response": {
        "Result": "{\"code\":0,\"data\":[{\"1737254300150\":1},{\"1737254310941\":1}],\"msg\":\"\",\"request_id\":\"65a8fec7-2b39-4b11-893f-3715279d235f\"}",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

