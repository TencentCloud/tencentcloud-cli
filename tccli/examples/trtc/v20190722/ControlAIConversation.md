**Example 1: 发送播报文本**

当您想让机器人主动播报文本的时候，可以使用该接口

Input: 

```
tccli trtc ControlAIConversation --cli-unfold-argument  \
    --TaskId your-taskid \
    --Command ServerPushText \
    --ServerPushText.Text 你好很高兴为您服务 \
    --ServerPushText.Interrupt True
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx-xxx"
    }
}
```

