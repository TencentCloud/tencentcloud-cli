**Example 1: 查询待处理异常进程事件趋势**



Input: 

```
tccli tcss DescribeAbnormalProcessEventTendency --cli-unfold-argument  \
    --EndTime 2021-05-01 \
    --StartTime 2021-05-07
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ProxyToolEventCount": 0,
                "RiskCmdEventCount": 0,
                "AttackCmdEventCount": 0,
                "UserDefinedRuleEventCount": 0,
                "TransferControlEventCount": 0,
                "AbnormalChildProcessEventCount": 0,
                "ReverseShellEventCount": 0,
                "FilelessEventCount": 0,
                "Date": "2020-09-22"
            }
        ],
        "RequestId": "xx"
    }
}
```

