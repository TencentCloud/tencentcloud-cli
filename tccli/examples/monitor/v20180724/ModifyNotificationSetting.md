**Example 1: 测试环境真实示例**



Input: 

```
tccli monitor ModifyNotificationSetting --cli-unfold-argument  \
    --MonitorType MT_CLS \
    --SettingId ntfs-3c5yw37f4oopcb9n \
    --MatchType PolicyOneOnOne \
    --MatchById policy-erictest2 \
    --HasEscalation False \
    --Notices.0.NoticeId notice-erictest \
    --Notices.0.ContentTmplId tmpl-erictest \
    --Notices.0.Levels None
```

Output: 
```
{
    "Response": {
        "RequestId": "afb342b4-bb31-407a-823a-52eb0513ced8"
    }
}
```

