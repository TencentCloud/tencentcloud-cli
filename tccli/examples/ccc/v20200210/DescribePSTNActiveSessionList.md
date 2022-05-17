**Example 1: 获取 PSTN 活动会话列表示例**



Input: 

```
tccli ccc DescribePSTNActiveSessionList --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --Offset 0 \
    --Limit 25
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "RequestId": "53bccf04-0870-4520-8614-f4bdddfd68df",
        "Sessions": [
            {
                "Direction": 1,
                "AcceptTimestamp": 1607702329,
                "ProtectedCaller": "",
                "RoomID": "32929373",
                "StartTimestamp": 1607702199,
                "Caller": "00864009282737",
                "ProtectedCallee": "",
                "StaffNumber": "1007",
                "SessionID": "0cf5be1b-de75-4445-a0c4-8dff3fa4b68b",
                "StaffEmail": "foo@tencent.com",
                "RingTimestamp": 1607702299,
                "Callee": "00864001783747",
                "SessionStatus": "inProgress"
            }
        ]
    }
}
```

