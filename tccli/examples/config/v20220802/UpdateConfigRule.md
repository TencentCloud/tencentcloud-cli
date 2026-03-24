**Example 1: 编辑规则**

编辑规则

Input: 

```
tccli config UpdateConfigRule --cli-unfold-argument  \
    --RuleId cr-bdunf5kx3aywn0ac5bkk \
    --RuleName CAM访问管理子用户必须关联用户组 \
    --Description 帐号访问管理中用户至少关联一个用户组，则符合规则。 \
    --RiskLevel 3 \
    --TriggerType.0.MessageType ScheduledNotification \
    --TriggerType.0.MaximumExecutionFrequency TwentyFour_Hours
```

Output: 
```
{
    "Response": {
        "RequestId": "da85d5e2-4432-4f02-9863-0ab07adeff33"
    }
}
```

