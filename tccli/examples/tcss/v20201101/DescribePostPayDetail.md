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
                "PayTime": "2024-10-30 10:02:45",
                "CoresCnt": 1
            }
        ],
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe"
    }
}
```

