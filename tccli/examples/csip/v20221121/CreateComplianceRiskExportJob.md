**Example 1: 创建合规标准和条款聚合风险导出任务**



Input: 

```
tccli csip CreateComplianceRiskExportJob --cli-unfold-argument  \
    --StandardID 3 \
    --MemberId mem-0addsds \
    --Limit 1 \
    --Offset 0 \
    --Order Desc \
    --By UpdateTime \
    --TermID 482
```

Output: 
```
{
    "Response": {
        "JobId": "a701cde3-8a97-4ea1-8592-af095c45e5b0",
        "RequestId": "6f852ba8-36b2-4a2f-a756-4d3e1fda6b6a"
    }
}
```

