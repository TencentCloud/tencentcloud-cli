**Example 1: 修改渠道信息**

修改渠道信息

Input: 

```
tccli adp ModifyChannel --cli-unfold-argument  \
    --AppId 20*************7712 \
    --ChannelId 207**68*********392 \
    --Scene 1 \
    --Spec.Scene 1 \
    --Spec.WecomRobot.Websocket.BindType 1 \
    --Spec.WecomRobot.Websocket.BotId aib**F***************Y1ldolKHwOOYCW \
    --Spec.WecomRobot.Websocket.BotSecret Xyd********QA*******I6GNX0or57z98TidPUyIJR6 \
    --UpdateMask.Paths Spec.WecomRobot.Websocket.BotId
```

Output: 
```
{
    "Response": {
        "RequestId": "eed79ed8-edfa-430e-9956-f26c0b385d97"
    }
}
```

