**Example 1: 发送模板邮件**

 

Input: 

```
tccli ses SendEmail --cli-unfold-argument  \
    --FromEmailAddress QCLOUDTEAM <noreply@mail.qcloud.com> \
    --ReplyToAddresses qcloud@tencent.com \
    --Destination user@example.com \
    --Template.TemplateID 100091 \
    --Template.TemplateData {"code":"1234"} \
    --Subject YourTestSubject
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "MessageId": "qcloud-ses-messageid"
    }
}
```

**Example 2: 发送富文本邮件**

 

Input: 

```
tccli ses SendEmail --cli-unfold-argument  \
    --FromEmailAddress QCLOUDTEAM <noreply@mail.qcloud.com> \
    --ReplyToAddresses qcloud@tencent.com \
    --Destination user@example.com \
    --Simple.Html PGh0bWw+PGRpdj5IZWxsb1dvcmxkPC9kaXY+PC9odG1sPg== \
    --Simple.Text aGVsbG8gd29ybGQ= \
    --Subject YourTestSubject
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "MessageId": "qcloud-ses-messageid"
    }
}
```

**Example 3: 发送纯文本邮件**

 

Input: 

```
tccli ses SendEmail --cli-unfold-argument  \
    --FromEmailAddress QCLOUDTEAM <noreply@mail.qcloud.com> \
    --ReplyToAddresses qcloud@tencent.com \
    --Destination user@example.com \
    --Simple.Text aGVsbG8gd29ybGQ= \
    --Subject YourTestSubject
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "MessageId": "qcloud-ses-messageid"
    }
}
```

