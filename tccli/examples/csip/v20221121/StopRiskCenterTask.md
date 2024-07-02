**Example 1: 停止扫风险中心扫描任务**

停止扫风险中心扫描任务

Input: 

```
tccli csip StopRiskCenterTask --cli-unfold-argument  \
    --MemberId abcd \
    --TaskIdList.0.TaskId rmis-abcd
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "RequestId": "abcd"
    }
}
```

