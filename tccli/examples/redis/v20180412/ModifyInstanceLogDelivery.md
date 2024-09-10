**Example 1: 示例1**

开启实例日志投递，并使用新创建的日志集和日志主题

Input: 

```
tccli redis ModifyInstanceLogDelivery --cli-unfold-argument  \
    --InstanceId crs-ib4uuh7x \
    --LogType slowlog \
    --Enabled True \
    --LogsetName test-logset-name \
    --TopicName test-topic-name \
    --CreateIndex True
```

Output: 
```
{
    "Response": {
        "RequestId": "ac46037a-57a0-4fe2-a99d-93c10ef20883"
    }
}
```

