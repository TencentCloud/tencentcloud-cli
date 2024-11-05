**Example 1: 删除风险中心扫描任务**

删除风险中心扫描任务

Input: 

```
tccli csip DeleteRiskScanTask --cli-unfold-argument  \
    --MemberId mem-******** \
    --TaskIdList.0.TaskId rmis-****
```

Output: 
```
{
    "Response": {
        "RequestId": "7429061e-dabd-e1ee-e135-43364c7bb15d"
    }
}
```

