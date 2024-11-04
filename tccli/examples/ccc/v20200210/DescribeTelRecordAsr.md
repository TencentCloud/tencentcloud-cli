**Example 1: 拉取录音信息**



Input: 

```
tccli ccc DescribeTelRecordAsr --cli-unfold-argument  \
    --SdkAppId 1400000000 \
    --SessionId 6bb56a09-2787-40bc-80c5-dc6dab783eff
```

Output: 
```
{
    "Response": {
        "RequestId": "6bb56a09-2787-40bc-80c5-dc6dab783eff",
        "AsrDataList": [
            {
                "User": "foo@tencent.com",
                "Message": "测试会话",
                "Start": 1729697242236,
                "End": 1729697245426
            }
        ]
    }
}
```

