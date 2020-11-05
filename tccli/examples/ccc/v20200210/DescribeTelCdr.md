**Example 1: 获取电话话单示例**



Input: 

```
tccli ccc DescribeTelCdr --cli-unfold-argument  \
    --SdkAppId 1400000000\
    --StartTimeStamp 1590547606\
    --EndTimeStamp 1590147606\
    --Limit 10\
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "6bb56a09-2787-40bc-80c5-dc6dab783eff",
        "TotalCount": 2,
        "TelCdrs": [
            {
                "Caller": "12345678901",
                "Callee": "23456789011",
                "Time": 1590547606,
                "Direction": 0,
                "Duration": 60,
                "RecordURL": "http://recorder-10018504.cos.ap-shanghai.myqcloud.com/def/month12/000-890990948-12364-58b657a6c5dd4c28b4f033b56716f686-000-157863356.mp3",
                "EndStatus": 1,
                "SkillGroup": "test",
                "SeatUser": {
                    "Name": "zhangsan",
                    "Phone": "12321233455"
                },
                "CallerLocation": "广东深圳"
            },
            {
                "Caller": "12345678902",
                "Callee": "23456789011",
                "Time": 1590547630,
                "Direction": 0,
                "Duration": 62,
                "RecordURL": "http://recorder-10018504.cos.ap-shanghai.myqcloud.com/def/month12/000-890990948-12364-58b657a6c5dd4c28b4f033b56716f686-000-157863357.mp3",
                "EndStatus": 1,
                "SkillGroup": "test",
                "SeatUser": {
                    "Name": "wangwu",
                    "Phone": "12321233456"
                },
                "CallerLocation": "广东深圳"
            }
        ]
    }
}
```

