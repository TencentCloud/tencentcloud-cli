**Example 1: 查询漏洞风险高级配置**

	
查询漏洞风险高级配置

Input: 

```
tccli csip DescribeVULRiskAdvanceCFGList --cli-unfold-argument  \
    --MemberId abc \
    --TaskId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "RiskId": "abc",
                "VULName": "abc",
                "RiskLevel": "abc",
                "EMGCVulType": 0,
                "CheckFrom": "abc",
                "Enable": 0,
                "VULType": "abc",
                "ImpactVersion": "abc",
                "CVE": "abc",
                "VULTag": [
                    "abc"
                ],
                "FixMethod": [
                    "abc"
                ],
                "ReleaseTime": "abc"
            }
        ],
        "TotalCount": 0,
        "RiskLevelLists": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "VULTypeLists": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "CheckFromLists": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "VulTagList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

