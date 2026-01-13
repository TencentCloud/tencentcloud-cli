**Example 1: 获取合同审查记录列表web页面**



Input: 

```
tccli ess DescribeContractReviewTaskListWebUrl --cli-unfold-argument  \
    --Operator.UserId yzDUUckpfotltUxgD3IvZBJBdg
```

Output: 
```
{
    "Response": {
        "RequestId": "91d49357-6b70-4d58-8305-3c0e1093f53b",
        "WebUrl": "https://embed.test.qian.tencent.cn/ai-contract-review?embed=1&code=yDtO7UUckpft9uvqUxJPqXty5Qv8S45X&channel=TENCENTCLOUD&embedType=CONTRACT_REVIEW&action=DescribeTaskList&shortKey=yDtO7UAApEKYWCovDlfd"
    }
}
```

