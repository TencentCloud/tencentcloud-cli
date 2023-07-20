**Example 1: 例子**

例子

Input: 

```
tccli wedata EditBaseline --cli-unfold-argument  \
    --ProjectId abc \
    --BaselineName abc \
    --BaselineType abc \
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
    --BaselineId abc \
    --UpdateUin abc \
    --UpdateName abc \
    --BaselineModifyAlarmRuleRequest.AlarmId abc \
    --BaselineModifyAlarmRuleRequest.RuleName abc \
    --BaselineModifyAlarmRuleRequest.MonitorType 0 \
    --BaselineModifyAlarmRuleRequest.MonitorObjectIds abc \
    --BaselineModifyAlarmRuleRequest.AlarmTypes abc \
    --BaselineModifyAlarmRuleRequest.AlarmLevel 0 \
    --BaselineModifyAlarmRuleRequest.AlarmWays abc \
    --BaselineModifyAlarmRuleRequest.AlarmRecipientType 0 \
    --BaselineModifyAlarmRuleRequest.AlarmRecipients abc \
    --BaselineModifyAlarmRuleRequest.AlarmRecipientIds abc \
    --BaselineModifyAlarmRuleRequest.ExtInfo abc \
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

