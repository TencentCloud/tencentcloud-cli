**Example 1: 查询主机入侵检测事件统计**

查询主机入侵检测事件统计

Input: 

```
tccli cwp DescribeMachineRiskCnt --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "PrivilegeEscalation": 1,
        "Malware": 1,
        "ReverseShell": 1,
        "BruteAttack": 1,
        "MaliciousRequest": 1,
        "HostLogin": 1,
        "RequestId": "dfeffewafewahr4325fs",
        "Bash": 1
    }
}
```

