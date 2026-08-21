**Example 1: 查询 default 命名空间下的函数**



Input: 

```
tccli csip DescribeSCFFunctionList --cli-unfold-argument  \
    --SCFRegion ap-guangzhou \
    --Namespace default \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "FunctionId": "lam-abcdefgh",
                "FunctionName": "notify-webhook",
                "Namespace": "default",
                "Status": "Active",
                "Type": "Event"
            }
        ],
        "TotalCount": 1,
        "RequestId": "d3b7c5a1-6e4f-2d8a-9c1b-f5e3a7d2b8c6"
    }
}
```

