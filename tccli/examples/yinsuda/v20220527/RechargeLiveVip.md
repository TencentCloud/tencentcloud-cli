**Example 1: 充值直播会员**

为用户充值直播会员

Input: 

```
tccli yinsuda RechargeLiveVip --cli-unfold-argument  \
    --AppName test \
    --UserId test \
    --TradeSerialNo TradeSerialNo1 \
    --RoomId 123 \
    --VipDays 31 \
    --GiveType room_card
```

Output: 
```
{
    "Response": {
        "LiveVipUserInfo": {
            "LiveVipEndTime": "2023-07-10T18:17:37+08:00",
            "LiveVipStatus": "LiveVip"
        },
        "RequestId": "RequestId"
    }
}
```

