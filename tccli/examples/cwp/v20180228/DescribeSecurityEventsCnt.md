**Example 1: 获取安全事件数统计数据**

获取安全事件数统计数据

Input: 

```
tccli cwp DescribeSecurityEventsCnt --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Malware": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "EventsCount": 1,
        "ReverseShell": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "BaseLine": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "BruteAttack": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "EffectMachineCount": 1,
        "EmergencyVul": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "SysVul": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "PrivilegeRules": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "RiskDns": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "HostLogin": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "RequestId": "06eea0c1-7f08-41ba-a75e-8b2500e16bdf ",
        "AttackLogs": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "WindowVul": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "LinuxVul": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "Bash": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "WebVul": {
            "EventCnt": 1,
            "UuidCnt": 1
        }
    }
}
```

