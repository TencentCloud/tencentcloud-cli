**Example 1: 获取dataloginfo信息**



Input: 

```
tccli rum DescribeDataLogUrlInfo --cli-unfold-argument  \
    --ID 1 \
    --StartTime 1625444040 \
    --EndTime 1625454840
```

Output: 
```
{
    "Response": {
        "Result": "{\"request_id\":\"65a8fec7-2b39-4b11-893f-3715279d235f\",\"results\":[{\"statement_id\":0,\"total\":0},{\"statement_id\":1,\"total\":0}]}",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

