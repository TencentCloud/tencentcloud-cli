**Example 1: 新增批量自动发送任务**



Input: 

```
tccli ses BatchSendEmailWithReceiverDetail --cli-unfold-argument  \
    --TimedParam.BeginTime 2021-09-10 11:10:11 \
    --FromEmailAddress abc@bbc.com \
    --ReplyToAddresses abc@bbc.com \
    --ReceiverId 123 \
    --Template.TemplateData {"name":"123"} \
    --Template.TemplateID 1 \
    --CycleParam.IntervalTime 1 \
    --CycleParam.BeginTime 2021-09-10 11:10:11 \
    --Subject 邮件主题 \
    --TaskType 1 \
    --ADLocation 0 \
    --EmailDatas.0.Email 456@bc.com \
    --EmailDatas.0.TemplateData {"name":"aa","age":"12"}
```

Output: 
```
{
    "Response": {
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "TaskId": 1
    }
}
```

