**Example 1: 获取 PSTN 会话信息**



Input: 

```
tccli ccc DescribeTelSession --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SessionId 0cf5be1b-de75-4445-a0c4-8dff3fa4b68b
```

Output: 
```
{
    "Response": {
        "RequestId": "53bccf04-0870-4520-8614-f4bdddfd68df",
        "Session": {
            "SessionID": "0cf5be1b-de75-4445-a0c4-8dff3fa4b68b",
            "RoomID": "32929373",
            "Caller": "00864009282737",
            "Callee": "00864001783747",
            "StartTimestamp": 1607702199,
            "RingTimestamp": 1607702299,
            "AcceptTimestamp": 1607702329,
            "StaffEmail": "foo@tencent.com",
            "StaffNumber": "1007",
            "SessionStatus": "inProgress",
            "Direction": 1,
            "OutBoundCaller": "",
            "OutBoundCallee": "",
            "ProtectedCallee": "",
            "ProtectedCaller": ""
        }
    }
}
```

