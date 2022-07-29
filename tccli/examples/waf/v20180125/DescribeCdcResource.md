**Example 1: 查询示例**



Input: 

```
tccli waf DescribeCdcResource --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values 010000000 \
    --Filters.0.Name xx \
    --Filters.0.ExactMatch False \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "List": [
            {
                "Status": 0,
                "Ip": "xx",
                "ClusterId": "xx",
                "Auth": "xx",
                "ModifyTime": "2020-09-22T00:00:00+00:00",
                "Port": 1,
                "Type": "xx",
                "CreateTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "xx"
    }
}
```

