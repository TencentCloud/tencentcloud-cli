**Example 1: 发送播报文本**

当您想让机器人主动播报文本的时候，可以使用该接口

Input: 

```
tccli ccc ControlAIConversation --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SessionId 6bb56a09-2787-40bc-80c5-dc6dab783eff \
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

