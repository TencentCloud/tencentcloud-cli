**Example 1: 查询 LLM 审计系统规则列表示例**



Input: 

```
tccli csip DescribeSandboxLLMAuditSystemRuleList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "LLMRules": [
            {
                "RuleID": "grl-safety-politics-std",
                "RuleName": "涉政内容-标准",
                "Description": "检测输出中的涉政敏感内容（标准级别）"
            }
        ],
        "ToolCallRules": [
            {
                "RuleID": "gtc-baseline-001",
                "RuleName": "高危系统命令工具阻断",
                "Description": "拦截 rm -rf /、mkfs 格式化设备、dd 覆写块设备、shutdown/reboot 关机重启等确定性破坏命令"
            }
        ],
        "RequestId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
    }
}
```

