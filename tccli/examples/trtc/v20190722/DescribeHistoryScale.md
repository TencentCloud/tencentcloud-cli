**Example 1: 查询历史房间和用户数**



Input: 

```
tccli trtc DescribeHistoryScale --cli-unfold-argument  \
    --StartTime 1590065777 \
    --SdkAppId 1400353843 \
    --EndTime 1590065877
```

Output: 
```
{
    "Response": {
        "Total": 4,
        "ScaleList": [
            {
                "Time": 1587830400,
                "RoomNumbers": 130644,
                "UserNumber": 2111978,
                "UserCount": 7004243
            },
            {
                "Time": 1587744000,
                "RoomNumbers": 79241,
                "UserNumber": 781494,
                "UserCount": 2968232
            },
            {
                "Time": 1587657600,
                "RoomNumbers": 180341,
                "UserNumber": 3047931,
                "UserCount": 10839565
            },
            {
                "Time": 1587571200,
                "RoomNumbers": 185469,
                "UserNumber": 3267726,
                "UserCount": 11656700
            }
        ],
        "RequestId": "70259dd1-c935-4a31-8576-f4daadd942ef"
    }
}
```

