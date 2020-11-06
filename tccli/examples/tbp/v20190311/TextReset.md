**Example 1: 机器人对话服务接口**



Input: 

```
tccli tbp TextReset --cli-unfold-argument  \
    --BotId 972445 \
    --TerminalId 123
```

Output: 
```
{
    "Response": {
        "RequestId": "20190117150912",
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
        "SessionAttributes": "",
        "InputText": "北京"
    }
}
```

