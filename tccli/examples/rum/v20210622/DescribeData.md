**Example 1: 转发获取data信息**



Input: 

```
tccli rum DescribeData --cli-unfold-argument  \
    --ID 1 \
    --Query '"select delta(count) as allCount from db.name where time >'
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

