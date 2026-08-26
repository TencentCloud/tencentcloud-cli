**Example 1: 查询 LLM 审计告警列表示例**



Input: 

```
tccli csip DescribeSandboxLLMAuditAlertList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ID": 9001,
                "BelongAssetType": "HOST",
                "RuleID": 6001,
                "RuleName": "敏感意图审计",
                "SystemRuleName": "涉政内容-标准",
                "InstanceId": "ins-a1b2c3d4",
                "InstanceName": "app-server-01",
                "ClusterId": "",
                "ContainerId": "",
                "ContainerName": "",
                "HitPayload": "风险类型:越狱提示词,风险内容:用户询问越狱方法",
                "RuleAction": "BLOCK",
                "Level": "HIGH",
                "Status": "BLOCK",
                "FirstAlertTime": "2025-03-10T08:00:00+08:00",
                "LastAlertTime": "2025-03-15T14:30:00+08:00"
            }
        ],
        "TotalCount": 42,
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

