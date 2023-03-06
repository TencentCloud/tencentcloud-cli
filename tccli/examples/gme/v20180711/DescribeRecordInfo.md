**Example 1: 查询录制**

查询录制

Input: 

```
tccli gme DescribeRecordInfo --cli-unfold-argument  \
    --TaskId 446192236330927912 \
    --BizId 3400352518
```

Output: 
```
{
    "Response": {
        "RoomId": "7743",
        "RecordMode": 1,
        "RecordInfo": [
            {
                "RecordStatus": 2,
                "RecordBeginTime": 1234567868,
                "UserId": "6787",
                "FileName": "/3400352518_2314_447947346201176660_9081"
            }
        ],
        "RequestId": "h9167d24-a2c6-1125-a5bd-5c023ba721c2"
    }
}
```

