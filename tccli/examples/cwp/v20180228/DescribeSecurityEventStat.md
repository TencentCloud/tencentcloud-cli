**Example 1: 获取安全事件统计**



Input: 

```
tccli cwp DescribeSecurityEventStat --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "MachineTotalAffectNum": 28,
        "InvasionTotalAffectNum": 22,
        "VulTotalAffectNum": 5,
        "BaseLineTotalAffectNum": 5,
        "CyberAttackTotalAffectNum": 0,
        "MalwareStat": {
            "EventsNum": 352,
            "MachineAffectNum": 9
        },
        "HostLoginStat": {
            "EventsNum": 57,
            "MachineAffectNum": 10
        },
        "BruteAttackStat": {
            "EventsNum": 5,
            "MachineAffectNum": 3
        },
        "MaliciousRequestStat": {
            "EventsNum": 20,
            "MachineAffectNum": 4
        },
        "PrivilegeStat": {
            "EventsNum": 32,
            "MachineAffectNum": 5
        },
        "ReverseShellStat": {
            "EventsNum": 2,
            "MachineAffectNum": 1
        },
        "HighRiskBashStat": {
            "EventsNum": 179,
            "MachineAffectNum": 8
        },
        "AttackLogsStat": {
            "EventsNum": 0,
            "MachineAffectNum": 0
        },
        "VulRiskStat": {
            "EventsNum": 3,
            "MachineAffectNum": 2
        },
        "VulHighStat": {
            "EventsNum": 18,
            "MachineAffectNum": 5
        },
        "VulNormalStat": {
            "EventsNum": 13,
            "MachineAffectNum": 4
        },
        "VulLowStat": {
            "EventsNum": 1,
            "MachineAffectNum": 1
        },
        "BaselineRiskStat": {
            "EventsNum": 0,
            "MachineAffectNum": 0
        },
        "BaselineHighStat": {
            "EventsNum": 107,
            "MachineAffectNum": 5
        },
        "BaselineNormalStat": {
            "EventsNum": 653,
            "MachineAffectNum": 5
        },
        "BaselineLowStat": {
            "EventsNum": 128,
            "MachineAffectNum": 5
        },
        "VulStat": {
            "EventsNum": 8,
            "MachineAffectNum": 5
        },
        "Score": 20,
        "RequestId": "8c952399-b255-3711-1c3c-a5c8a6befbd8"
    }
}
```

