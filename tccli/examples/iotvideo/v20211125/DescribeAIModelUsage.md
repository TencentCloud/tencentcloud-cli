**Example 1: 查看AI模型资源包**



Input: 

```
tccli iotvideo DescribeAIModelUsage --cli-unfold-argument  \
    --Offset 0 \
    --ProductId test \
    --Limit 1 \
    --ModelId body_detect
```

Output: 
```
{
    "Response": {
        "UsageInfo": [
            {
                "Used": 100,
                "CreateTime": 1625555521,
                "Total": 100000
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

