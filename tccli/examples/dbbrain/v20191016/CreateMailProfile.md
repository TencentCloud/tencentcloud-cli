**Example 1: 创建定期生成/数据库巡检的邮件发送模板**

创建定期生成/数据库巡检的邮件发送模板。

Input: 

```
tccli dbbrain CreateMailProfile --cli-unfold-argument  \
    --Product mysql \
    --ProfileLevel Instance \
    --ProfileName scheduler_cdb-test \
    --ProfileType ' scheduler_mail_configuration' \
    --BindInstanceIds cdb-test \
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

