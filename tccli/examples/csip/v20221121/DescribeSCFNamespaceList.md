**Example 1: 查询广州地域 SCF 命名空间**



Input: 

```
tccli csip DescribeSCFNamespaceList --cli-unfold-argument  \
    --SCFRegion ap-guangzhou \
    --Limit 20 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Name": "default",
                "Type": "Default"
            },
            {
                "Name": "notify-ns",
                "Type": "Default"
            }
        ],
        "TotalCount": 2,
        "RequestId": "d3b7c5a1-6e4f-2d8a-9c1b-f5e3a7d2b8c6"
    }
}
```

