**Example 1: 例子**

例子

Input: 

```
tccli wedata CreateBaseline --cli-unfold-argument  \
    --ProjectId abc \
    --BaselineName abc \
    --BaselineType abc \
    --CreateUin abc \
    --CreateName abc \
    --InChargeUin abc \
    --InChargeName abc \
    --PromiseTasks.0.ProjectId abc \
    --PromiseTasks.0.TaskName abc \
    --PromiseTasks.0.TaskId abc \
    --PromiseTasks.0.TaskCycle abc \
    --PromiseTasks.0.WorkflowName abc \
    --PromiseTasks.0.WorkflowId abc \
    --PromiseTasks.0.TaskInChargeName abc \
    --PromiseTasks.0.TaskInChargeUin abc \
    --PromiseTime abc \
    --WarningMargin 1 \
    --AlarmRuleDto.AlarmRuleId abc \
    --AlarmRuleDto.AlarmLevelType abc \
    --BaselineCreateAlarmRuleRequest.ProjectId abc \
    --BaselineCreateAlarmRuleRequest.CreatorId abc \
    --BaselineCreateAlarmRuleRequest.Creator abc \
    --BaselineCreateAlarmRuleRequest.RuleName abc \
    --BaselineCreateAlarmRuleRequest.MonitorType 0 \
    --BaselineCreateAlarmRuleRequest.MonitorObjectIds abc \
    --BaselineCreateAlarmRuleRequest.AlarmTypes abc \
    --BaselineCreateAlarmRuleRequest.AlarmLevel 0 \
    --BaselineCreateAlarmRuleRequest.AlarmWays abc \
    --BaselineCreateAlarmRuleRequest.AlarmRecipientType 0 \
    --BaselineCreateAlarmRuleRequest.AlarmRecipients abc \
    --BaselineCreateAlarmRuleRequest.AlarmRecipientIds abc \
    --BaselineCreateAlarmRuleRequest.ExtInfo abc \
    --IsNewAlarm True
```

Output: 
```
{
    "Response": {
        "Data": {
            "Success": true,
            "Message": "abc"
        },
        "RequestId": "abc"
    }
}
```

