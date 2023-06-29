**Example 1: 获取直播会员充值记录信息列表**

获取直播会员充值记录信息列表

Input: 

```
tccli yinsuda DescribeLiveVipTradeInfos --cli-unfold-argument  \
    --AppName test \
    --StartTime 2023-01-22T00:00:00+00:00 \
    --EndTime 2023-02-22T00:00:00+00:00 \
    --TradeSerialNos no1 \
    --UserIds user1 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "LiveVipTradeInfoSet": [
            {
                "TradeSerialNo": "no1",
                "AppName": "test1",
                "UserId": "1",
                "RoomId": "12",
                "VipDays": 31,
                "Status": "Success",
                "CreateTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

