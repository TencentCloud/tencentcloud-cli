**Example 1: 正常请求1**

创建渠道

Input: 

```
tccli adp CreateChannel --cli-unfold-argument  \
    --AppId 20*************7392 \
    --Spec.ChannelName *****test_2 \
    --Spec.ChannelType 10014 \
    --Spec.Description ********t_desc \
    --Spec.Scene 1 \
    --Spec.UserAgent.AgentId user**********3********-a96b-a9217f6115** \
    --Spec.UserAgent.UserId **** \
    --Spec.WecomRobot.Websocket.BindType 2 \
    --Spec.WecomRobot.Websocket.BotId a*b*************g*****E**Cr7b_xze0a \
    --Spec.WecomRobot.Websocket.BotSecret f***********q***********GhEkxgJejFKl4mjPM*I
```

Output: 
```
{
    "Response": {
        "ChannelId": "20****8********2560",
        "QrcodeUrl": "ht**s*/**i*e***.w******qq**om/q/7GiQu1?qrcode****00****b6c*********************bot_type=3",
        "RequestId": "e1a33115-e3f9-4dda-b953-78ac0ec772b5"
    }
}
```

