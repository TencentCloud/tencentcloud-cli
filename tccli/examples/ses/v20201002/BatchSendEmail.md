**Example 1: 新增批量发送任务**

 

Input: 

```
tccli ses BatchSendEmail --cli-unfold-argument  \
    --Attachments.0.Content 附件内容 \
    --Attachments.0.FileName 文件名 \
    --TimedParam.BeginTime 2021-09-10 11:10:11 \
    --FromEmailAddress abc@bbc.com \
    --ReplyToAddresses abc@bbc.com \
    --Simple.Text text \
    --Simple.Html html \
    --ReceiverId 123 \
    --Template.TemplateData {"name":"123"} \
    --Template.TemplateID 1 \
    --CycleParam.IntervalTime 1 \
    --CycleParam.BeginTime 2021-09-10 11:10:11 \
    --Subject 邮件主题 \
    --TaskType 1 \
    --ADLocation 0
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "TaskId": 123
    }
}
```

