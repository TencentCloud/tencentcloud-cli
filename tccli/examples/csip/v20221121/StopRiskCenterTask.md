**Example 1: 停止扫风险中心扫描任务**

停止扫风险中心扫描任务

Input: 

```
tccli csip StopRiskCenterTask --cli-unfold-argument  \
    --TaskIdList.0.TaskId rmis-******
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "7c9179a6-1dbe-4ee6-933c-c53f5d3bb0d4"
    }
}
```

