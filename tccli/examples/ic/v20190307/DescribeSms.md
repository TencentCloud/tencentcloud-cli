**Example 1: 查询短信列表**



Input: 

```
tccli ic DescribeSms --cli-unfold-argument  \
    --Iccid 898607B0011700966351 \
    --Msisdn 1064702726351 \
    --Sdkappid 1400057107 \
    --SmsType 1 \
    --BeginTime 1970-01-01 \
    --EndTime 2019-11-30 \
    --Offset 0 \
    --Limit 3
```

Output: 
```
{
    "Response": {
        "RequestId": "3b74d269-cbb6-4d06-b2b0-0c6f0efe850a",
        "Total": 39,
        "List": [
            {
                "Iccid": "898607B0011700966351",
                "Msisdn": "1064702726351",
                "SdkAppid": 1400057107,
                "Content": "haha",
                "SmsType": 1,
                "SendTime": "2018-11-12 16:04:55",
                "ReportTime": "",
                "Remark": "",
                "Status": 3
            },
            {
                "Iccid": "898607B0011700966351",
                "Msisdn": "1064702726351",
                "SdkAppid": 1400057107,
                "Content": "haha",
                "SmsType": 1,
                "SendTime": "2018-11-12 15:58:32",
                "ReportTime": "2018-11-14 15:58:32",
                "Remark": "FAIL",
                "Status": 2
            },
            {
                "Iccid": "898607B0011700966351",
                "Msisdn": "1064702726351",
                "SdkAppid": 1400057107,
                "Content": "haha",
                "SmsType": 1,
                "SendTime": "2018-11-12 15:58:25",
                "ReportTime": "",
                "Remark": "",
                "Status": 3
            }
        ]
    }
}
```

