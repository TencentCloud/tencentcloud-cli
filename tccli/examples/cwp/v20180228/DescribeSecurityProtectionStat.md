**Example 1: 获取安全防护状态**



Input: 

```
tccli cwp DescribeSecurityProtectionStat --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AssetManageStat": 1,
        "SecureBasicLineStat": 1,
        "ExpertServiceStat": 1,
        "LoginLogStat": 1,
        "VulManageStat": 1,
        "FileTamperStat": 1,
        "WarningSetStat": 1,
        "DiscoverBruteAttackStat": 1,
        "DefenseBruteAttackStat": 1,
        "RequestId": "e79efea3-3f70-46c0-a7e1-ed38a2476098",
        "ReverseShellStat": 1,
        "LogAnalysisStat": 1,
        "PrivilegeStat": 1,
        "MalwareScanStat": 1,
        "WebPageStat": 1,
        "EventBashStat": 1,
        "MaliciousRequestStat": 1
    }
}
```

