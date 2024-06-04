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
            "RoomId": "awv5dis27j",
            "LiveVipEndTime": "2020-09-22T00:00:00+00:00",
            "LiveVipStatus": "Valid"
        },
        "RequestId": "abc"
    }
}
```

