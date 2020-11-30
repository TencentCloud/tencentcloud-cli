**Example 1: 获取安全事件数统计数据**

获取安全事件数统计数据

Input: 

```
tccli cwp DescribeSecurityEventsCnt --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AttackLogs": {
            "EventCnt": 439,
            "UuidCnt": 1
        },
        "BaseLine": {
            "EventCnt": 1353,
            "UuidCnt": 11
        },
        "Bash": {
            "EventCnt": 5911,
            "UuidCnt": 31
        },
        "BruteAttack": {
            "EventCnt": 52,
            "UuidCnt": 10
        },
        "EmergencyVul": {
            "EventCnt": 6,
            "UuidCnt": 5
        },
        "HostLogin": {
            "EventCnt": 169,
            "UuidCnt": 23
        },
        "Malware": {
            "EventCnt": 226,
            "UuidCnt": 12
        },
        "PrivilegeRules": {
            "EventCnt": 1,
            "UuidCnt": 1
        },
        "ReverseShell": {
            "EventCnt": 2,
            "UuidCnt": 1
        },
        "RiskDns": {
            "EventCnt": 5,
            "UuidCnt": 2
        },
        "SysVul": {
            "EventCnt": 25,
            "UuidCnt": 14
        },
        "WebVul": {
            "EventCnt": 3,
            "UuidCnt": 2
        },
        "RequestId": "1234567"
    }
}
```

