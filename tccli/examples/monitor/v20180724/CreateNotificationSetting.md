**Example 1: 测试环境真实示例**



Input: 

```
tccli monitor CreateNotificationSetting --cli-unfold-argument  \
    --MonitorType MT_CLS \
    --MatchType PolicyOneOnOne \
    --MatchById policy-erictest2 \
    --HasEscalation True \
    --Notices.0.NoticeId notice-erictest \
    --Notices.0.ContentTmplId tmpl-erictest \
    --Notices.0.Levels None \
    --EscalationRules.0.PartSeqNum 1 \
    --EscalationRules.0.Notices.0.NoticeId notice-erictest11 \
    --EscalationRules.0.Notices.0.ContentTmplId tmpl-erictest11 \
    --EscalationRules.0.Notices.0.Levels None \
    --EscalationRules.0.Notices.1.NoticeId notice-erictest12 \
    --EscalationRules.0.Notices.1.ContentTmplId tmpl-erictest12 \
    --EscalationRules.0.Notices.1.Levels None \
    --EscalationRules.0.AfterLastPartSeconds 3000 \
    --EscalationRules.1.PartSeqNum 2 \
    --EscalationRules.1.Notices.0.NoticeId notice-erictest21 \
    --EscalationRules.1.Notices.0.ContentTmplId tmpl-erictest21 \
    --EscalationRules.1.Notices.0.Levels None \
    --EscalationRules.1.AfterLastPartSeconds 5000
```

Output: 
```
{
    "Response": {
        "RequestId": "569fe099-bb56-48d1-9ec2-41c22593b433",
        "SettingId": "ntfs-3c5yw37f4oopcb9n"
    }
}
```

