**Example 1: 拉取AI模型列表**



Input: 

```
tccli iotvideo DescribeAIModels --cli-unfold-argument  \
    --Status 1 \
    --Offset 0 \
    --Limit 1 \
    --ModelId body_detect
```

Output: 
```
{
    "Response": {
        "Models": [
            {
                "Status": 1,
                "ApprovalTime": 1625555521,
                "Used": 0,
                "ApplyTime": 1625555521,
                "ProductName": "test",
                "Total": 0,
                "ProductId": "testid"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

