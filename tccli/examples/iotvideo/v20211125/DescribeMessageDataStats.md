**Example 1: 查询设备消息数据统计**



Input: 

```
tccli iotvideo DescribeMessageDataStats --cli-unfold-argument  \
    --StartDate 2022-06-11 \
    --EndDate 2022-06-13 \
    --ProductId L78xxxxZ95
```

Output: 
```
{
    "Response": {
        "RequestId": "ea134bab-41c7-426c-bfd9-559f453893db",
        "Data": [
            {
                "Date": "2022-06-11",
                "UpMsgCnt": 0,
                "DownMsgCnt": 0,
                "NtpMsgCnt": 0
            },
            {
                "Date": "2022-06-12",
                "UpMsgCnt": 0,
                "DownMsgCnt": 0,
                "NtpMsgCnt": 0
            },
            {
                "Date": "2022-06-13",
                "UpMsgCnt": 0,
                "DownMsgCnt": 0,
                "NtpMsgCnt": 0
            }
        ],
        "Total": 3
    }
}
```

