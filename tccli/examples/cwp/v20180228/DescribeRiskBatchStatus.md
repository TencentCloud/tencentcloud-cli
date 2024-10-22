**Example 1: 查询入侵检测事件更新状态任务是否完成**



Input: 

```
tccli cwp DescribeRiskBatchStatus --cli-unfold-argument  \
    --RiskType MALWARE
```

Output: 
```
{
    "Response": {
        "Status": "Handling",
        "RequestId": "1703764f-b3ea-4d7f-99cb-cc3a6a62e2ec"
    }
}
```

