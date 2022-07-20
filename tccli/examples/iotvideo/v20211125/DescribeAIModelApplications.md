**Example 1: 用户AI模型申请记录**



Input: 

```
tccli iotvideo DescribeAIModelApplications --cli-unfold-argument  \
    --Offset 0 \
    --ProductId test \
    --Limit 1 \
    --ModelId body_detect
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RequestId": "xx",
        "Applications": [
            {
                "Status": 1,
                "ProductName": "name",
                "ProductId": "test"
            }
        ]
    }
}
```

