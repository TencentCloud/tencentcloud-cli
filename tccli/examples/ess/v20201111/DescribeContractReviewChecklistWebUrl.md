**Example 1: 查看审查要点清单web页面**



Input: 

```
tccli ess DescribeContractReviewChecklistWebUrl --cli-unfold-argument  \
    --Operator.UserId yDtzUckfhotlUxpgD3vZBB10dg \
    --Id yDzlUckpfqqe0eU7RX5uRpuL6kx
```

Output: 
```
{
    "Response": {
        "Id": "yDzlUckpfqqe0eU7RX5uRpuL6kx",
        "RequestId": "25c04cf7-cfb4-4fc1-9c00-493bf4d57f5f",
        "WebUrl": "https://embed.test.qian.tencent.cn/ai-contract-review?embed=1&code=yDtO7UUckpft9kelUuJKYGa1CXDMNbuW&channel=TENCENTCLOUD&embedType=CONTRACT_REVIEW&action=DescribeChecklist&shortKey=yDtO7UAApy9YcVs8cga0&checklistId=yDtzlUUckpfqqe0eUx7RX5uRp4uL96kx"
    }
}
```

