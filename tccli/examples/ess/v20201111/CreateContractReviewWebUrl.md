**Example 1: 创建合同审查web页面**



Input: 

```
tccli ess CreateContractReviewWebUrl --cli-unfold-argument  \
    --Operator.UserId yDwqbUUckp3oxxo7 \
    --ResourceId yDt4oUUcxxxqVZx \
    --UserData 5rWL6K+V5pWw5o2u
```

Output: 
```
{
    "Response": {
        "RequestId": "s1755568206750403220",
        "TaskId": "yDt4mUUckp9sgohiUugsjbKR241Yq5F7",
        "WebUrl": "https://embed.test.qian.tencent.cn/ai-contract-review?embed=1&code=yDt4oUUckp9sdhe2UugPqwK8NOCXY1Rg&channel=TENCENTCLOUD&embedType=CONTRACT_REVIEW&shortKey=yDt4mUjbKxHBzcYpadbe"
    }
}
```

