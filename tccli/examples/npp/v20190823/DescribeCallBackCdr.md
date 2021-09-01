**Example 1: 示例**



Input: 

```
tccli npp DescribeCallBackCdr --cli-unfold-argument  \
    --BizAppId xxx \
    --CallId xxxx \
    --Dst xxxx \
    --StartTimeStamp 1577030400 \
    --EndTimeStamp 1577116799
```

Output: 
```
{
    "Response": {
        "Cdr": [
            {
                "BizId": "",
                "CallEndStatus": "1",
                "CallId": "xxxxx",
                "CallType": "3",
                "Dst": "008613xxxxxxx",
                "DstAcceptTime": "1577082673",
                "Duration": "13",
                "EndCallTime": "1577082678",
                "OrderId": "",
                "RecordUrl": "url",
                "Src": "00861xxxxxxx",
                "SrcAcceptTime": "1577082658",
                "StartDstCallTime": "1577082658",
                "StartDstRingTime": "1577082658",
                "StartSrcCallTime": "1577082644",
                "StartSrcRingTime": "1577082644"
            }
        ],
        "ErrorCode": "0",
        "Msg": "Call Details",
        "Offset": "0",
        "RequestId": "e72179b7-9e82-4bcf-a62d-523d5baf571f"
    }
}
```

