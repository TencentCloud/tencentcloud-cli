**Example 1: 机器人对话服务接口**

重置机器人的会话状态

Input: 

```
tccli tbp Reset --cli-unfold-argument  \
    --BotId 972445 \
    --BotVersion dev \
    --UserId 123
```

Output: 
```
{
    "Response": {
        "RequestId": "20190117150912",
        "Error": {
            "Code": "",
            "Message": ""
        },
        "DialogStatus": "COMPLETE",
        "BotName": "订票机器人",
        "IntentName": "Intent_book_tickets",
        "ResponseText": "好的，我这就去办。",
        "SlotInfoList": [
            {
                "SlotName": "CityName",
                "SlotValue": "北京"
            }
        ],
        "WaveData": "",
        "SessionAttributes": "",
        "Question": "北京",
        "WaveUrl": "http://stevinpan-chatflow-1255628450.cos.ap-guangzhou.myqcloud.com/100008/123/1551412004.pcm"
    }
}
```

