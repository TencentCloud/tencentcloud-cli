**Example 1: 查询后付费详情**



Input: 

```
tccli tcss DescribePostPayDetail --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "SoftQuotaDayDetail": [
            {
                "PayTime": "xx",
                "CoresCnt": 1
            }
        ],
        "RequestId": "xx"
    }
}
```

