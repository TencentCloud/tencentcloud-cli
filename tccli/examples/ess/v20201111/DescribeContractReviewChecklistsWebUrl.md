**Example 1: 获取审查要点清单列表web页面**



Input: 

```
tccli ess DescribeContractReviewChecklistsWebUrl --cli-unfold-argument  \
    --Operator.UserId yDtzUUckpfhotUxpgDvZBJB10dg \
    --Option.DisableCreateChecklist True
```

Output: 
```
{
    "Response": {
        "RequestId": "917685ef-08bf-47d0-848a-562b49104f87",
        "WebUrl": "https://embed.test.qian.tencent.cn/ai-contract-review?embed=1&code=yDtO7UUckpft9ol3UuJKYGaxv58BYWbB&channel=TENCENTCLOUD&embedType=CONTRACT_REVIEW&action=DescribeChecklists&shortKey=yDtO7UAApwRvM9OqBY62"
    }
}
```

