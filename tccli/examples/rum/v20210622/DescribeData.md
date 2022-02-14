**Example 1: 转发获取data信息**



Input: 

```
tccli rum DescribeData --cli-unfold-argument  \
    --ID 1 \
    --Query '"select delta(count) as allCount from pv_url_statistics where  time >'
```

Output: 
```
{
    "Response": {
        "Result": "xxxx",
        "RequestId": "65a8fec7-2b39-4b11-893f-3715279d235f"
    }
}
```

