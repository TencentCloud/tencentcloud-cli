**Example 1: 获取合同审查结果web页面**



Input: 

```
tccli ess DescribeContractReviewWebUrl --cli-unfold-argument  \
    --Operator.UserId yDwqbUUckp3o2rzmUxHsV0j1FlhYIKo7 \
    --TaskId yDt4MUUckp9j4zj5UugsjbKvB0vibmas
```

Output: 
```
{
    "Response": {
        "RequestId": "s1755602790251475316",
        "Status": 1,
        "WebUrl": "https://embed.test.qian.tencent.cn/ai-contract-review?embed=1&code=yDt4mUUckp9shfedUx7mkC9zwLgqGdH6&channel=TENCENTCLOUD&embedType=CONTRACT_REVIEW&taskId=yDt4mUUckp9sgohiUugsjbKR241Yq5F7&preTaskId=yDt4mUUckp9sgoh6UugsjbKsbOWqWA2o"
    }
}
```

