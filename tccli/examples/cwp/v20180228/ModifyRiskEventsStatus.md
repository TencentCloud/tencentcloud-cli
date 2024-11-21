**Example 1: 示例**

需要批量更新事件的状态时

Input: 

```
tccli cwp ModifyRiskEventsStatus --cli-unfold-argument  \
    --UpdateAll True \
    --RiskType MALWARE \
    --Ip 0.0.0.0 \
    --Ids 1 \
    --KillProcess True \
    --ExcludeId 1 \
    --Operate 1 \
    --DoClean False
```

Output: 
```
{
    "Response": {
        "RequestId": "a066ece3-12ca-4611-b98e-1c296a14a491",
        "IsSync": 1
    }
}
```

