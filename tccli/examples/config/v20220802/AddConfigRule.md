**Example 1: 添加规则**

添加规则

Input: 

```
tccli config AddConfigRule --cli-unfold-argument  \
    --Identifier cam-user-group-bound \
    --IdentifierType SYSTEM \
    --RuleName CAM访问管理子用户必须关联用户组 \
    --ResourceType QCS::CAM::User \
    --RiskLevel 3 \
    --Description 帐号访问管理中用户至少关联一个用户组，则符合规则。 \
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

