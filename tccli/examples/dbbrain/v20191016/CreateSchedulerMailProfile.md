**Example 1: 创建定期生成的邮件发送配置**

该接口用于创建定期生成健康报告并邮件发送的配置，将健康报告的定期生成时间作为参数传入（周一至周日），用于设置健康报告的定期生成时间，同时保存相应的定期邮件发送的配置。

Input: 

```
tccli dbbrain CreateSchedulerMailProfile --cli-unfold-argument  \
    --WeekConfiguration 1 \
    --Product mysql \
    --ProfileName scheduler_cdb-test \
    --BindInstanceId cdb-test \
    --ProfileInfo.Language zh \
    --ProfileInfo.MailConfiguration.SendMail 1 \
    --ProfileInfo.MailConfiguration.Region ap-guangzhou \
    --ProfileInfo.MailConfiguration.HealthStatus HEALTH \
    --ProfileInfo.MailConfiguration.ContactPerson 1 \
    --ProfileInfo.MailConfiguration.ContactGroup 1
```

Output: 
```
{
    "Response": {
        "RequestId": "77db16d7-bbe8-48a7-868b-ed776a96f1ab"
    }
}
```

