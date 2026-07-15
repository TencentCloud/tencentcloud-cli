**Example 1: 查询策略下发状态**



Input: 

```
tccli fwm DescribeStrategyDispatchStatus --cli-unfold-argument  \
    --Product enterprise_sg
```

Output: 
```
{
    "Response": {
        "DispatchStrategyList": [
            "fwms-kmbf8avt",
            "fwms-ms91jjvy",
            "fwms-vg9ji1r5"
        ],
        "EndTime": "2026-02-27 19:52:50",
        "ErrorMsg": "",
        "Progress": 100,
        "RequestId": "77659938-d469-4313-ba83-232b66559e1e",
        "RuleGroupNum": 3,
        "StartTime": "2026-02-27 19:52:35",
        "Status": 2
    }
}
```

