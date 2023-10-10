**Example 1: 示例**

需要批量更新事件的状态时

Input: 

```
tccli cwp ModifyRiskEventsStatus --cli-unfold-argument  \
    --UpdateAll True \
    --RiskType xx \
    --Ip xx \
    --Ids 1 \
    --KillProcess True \
    --ExcludeId 1 \
    --Operate 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "IsSync": 1
    }
}
```

