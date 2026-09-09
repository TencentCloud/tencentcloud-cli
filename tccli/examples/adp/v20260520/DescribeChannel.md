**Example 1: 查询渠道信息**

查询渠道信息

Input: 

```
tccli adp DescribeChannel --cli-unfold-argument  \
    --AppId 20****2********7712 \
    --ChannelId 20*****2*******9232 \
    --Scene 1
```

Output: 
```
{
    "Response": {
        "Channel": {
            "ChannelId": "20***6**********232",
            "ConnectStatus": 2,
            "CreateTime": "1784283158",
            "Spec": {
                "ChannelName": "*********_test_1",
                "ChannelType": 10015,
                "Description": "**********test_desc",
                "Scene": 1,
                "UserAgent": {
                    "AgentId": "user_***d*1****dd8**d*******-cf999d376482",
                    "UserId": "a********"
                },
                "WechatClawBot": {
                    "BotId": "c***7***1********ot",
                    "BotToken": "",
                    "QrcodeStatus": "confirmed",
                    "QrcodeUrl": "",
                    "WechatUserId": "o9****4**Nu**********Car*diI@im.wechat"
                }
            },
            "UpdateTime": "1784283158",
            "Updater": ""
        },
        "RequestId": "7abdf1cb-2a77-4284-b4c7-67b059dcd34f"
    }
}
```

