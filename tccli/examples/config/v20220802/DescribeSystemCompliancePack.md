**Example 1: 获取合规包详情**



Input: 

```
tccli config DescribeSystemCompliancePack --cli-unfold-argument  \
    --CompliancePackId cp-wn7attowki
```

Output: 
```
{
    "Response": {
        "CompliancePackId": "cp-wn7attowki",
        "CompliancePackName": "PCI-DSSu6570u636eu5b89u5168u6807u51c6u5408u89c4u5305",
        "ConfigRules": [
            {
                "CreateTime": "2023-07-14 09:08:20",
                "Description": "CBSu4e91u786cu76d8u5f00u542fu4e86u52a0u5bc6uff0cu5219u7b26u5408u89c4u5219",
                "Identifier": "cbs-disk-encrypted",
                "RiskLevel": 2,
                "RuleName": "CBSu4e91u786cu76d8u5f00u542fu52a0u5bc6u72b6u6001",
                "UpdateTime": "2023-09-11 18:04:45"
            }
        ],
        "Description": "u53c2u7167PCI DSS v4.0u5bf9u8d26u53f7u6570u636eu4fddu62a4u7684u57fau7eb***u9762u63d0u4f9bu90e8u5206u5efau8baeu7684u5408u89c4u6027u68c0u6d4bu3002",
        "RiskLevel": 1,
        "RequestId": "3b76f6ae-1cc6-455f-8073-409cbf34e186"
    }
}
```

