**Example 1: 云边界风险待治理风险**



Input: 

```
tccli csip DescribeExposeRiskStatistics --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ExposureRiskStatistics": [
            {
                "RiskCount": 3,
                "RuleType": "all_port_open",
                "Severity": "emergency",
                "Title": "全端口对公网开放"
            },
            {
                "RiskCount": 13,
                "RuleType": "use_high_risk_port",
                "Severity": "high",
                "Title": "使用了高危的端口号"
            },
            {
                "RiskCount": 3,
                "RuleType": "port_range_open",
                "Severity": "medium",
                "Title": "按端口范围对公网开放"
            },
            {
                "RiskCount": 23,
                "RuleType": "use_unstandard_port",
                "Severity": "low",
                "Title": "使用了非标的端口号"
            },
            {
                "RiskCount": 2,
                "RuleType": "unaccess_asset",
                "Severity": "low",
                "Title": "资产当前无法访问"
            }
        ],
        "RequestId": "036d871a-e1c0-409d-af42-f7e790038d59"
    }
}
```

