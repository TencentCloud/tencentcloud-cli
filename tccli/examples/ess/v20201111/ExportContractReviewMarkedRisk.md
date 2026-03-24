**Example 1: 批量导出人工创建或者标注（忽略，标记错误）的风险示例**



Input: 

```
tccli ess ExportContractReviewMarkedRisk --cli-unfold-argument  \
    --Operator.UserId yDRtvUUg*gqu**k7Uu*4*j***XVnuTnA \
    --FromDate 2025-12-01 \
    --ToDate 2025-12-28
```

Output: 
```
{
    "Response": {
        "TaskId": "yD3aDUUc*pm*u*nvUu*R*faSfh2BjyG9",
        "RequestId": "0c6804b9-155f-4a54-aad2-f10a0df4b90e"
    }
}
```

