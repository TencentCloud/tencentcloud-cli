**Example 1: 查询函数 notify-webhook 的别名**



Input: 

```
tccli csip DescribeSCFAliasList --cli-unfold-argument  \
    --SCFRegion ap-guangzhou \
    --Namespace default \
    --FunctionName notify-webhook \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Name": "prod",
                "FunctionVersion": "1"
            }
        ],
        "TotalCount": 1,
        "RequestId": "d3b7c5a1-6e4f-2d8a-9c1b-f5e3a7d2b8c6"
    }
}
```

