**Example 1: 修改全局告警通知渠道**

修改全局告警通知渠道

Input: 

```
tccli monitor ModifyPrometheusGlobalNotification --cli-unfold-argument  \
    --InstanceId abc \
    --Notification.Enabled True \
    --Notification.Type abc \
    --Notification.WebHook abc \
    --Notification.AlertManager.ClusterType abc \
    --Notification.AlertManager.ClusterId abc \
    --Notification.AlertManager.Url abc \
    --Notification.RepeatInterval abc \
    --Notification.TimeRangeStart abc \
    --Notification.TimeRangeEnd abc \
    --Notification.NotifyWay abc \
    --Notification.ReceiverGroups abc \
    --Notification.PhoneNotifyOrder 1 \
    --Notification.PhoneCircleTimes 0 \
    --Notification.PhoneInnerInterval 0 \
    --Notification.PhoneCircleInterval 0 \
    --Notification.PhoneArriveNotice True
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

