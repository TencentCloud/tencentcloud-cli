**Example 1: 删除风险中心扫描任务**

删除风险中心扫描任务

Input: 

```
tccli csip DeleteRiskScanTask --cli-unfold-argument  \
    --MemberId mem-abcd \
    --TaskIdList.0.TaskId abcd
```

Output: 
```
{
    "Response": {
        "RequestId": "abcd"
    }
}
```

