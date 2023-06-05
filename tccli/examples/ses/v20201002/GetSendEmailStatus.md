**Example 1: 根据MessageId查询发送结果**

 

Input: 

```
tccli ses GetSendEmailStatus --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --RequestDate 2020-09-22 \
    --MessageId qcloudses-30-4123414323-date-20210101094334-syNARhMTbKI1
```

Output: 
```
{
    "Response": {
        "EmailStatusList": [
            {
                "UserOpened": true,
                "UserUnsubscribed": true,
                "RequestTime": 1609831698,
                "UserComplainted": true,
                "ToEmailAddress": "example@cloud.com",
                "FromEmailAddress": "noreply@tencent.com",
                "UserClicked": true,
                "DeliverTime": 1609831698,
                "DeliverMessage": "",
                "MessageId": "qcloudses-30-4123414323-date-20210101094334-syNARhMTbKI1",
                "SendStatus": 0,
                "DeliverStatus": 0
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

**Example 2: 根据收件人查询发送结果**

 

Input: 

```
tccli ses GetSendEmailStatus --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --RequestDate 2020-09-22 \
    --ToEmailAddress example@cloud.com
```

Output: 
```
{
    "Response": {
        "EmailStatusList": [
            {
                "UserOpened": true,
                "UserUnsubscribed": true,
                "RequestTime": 1609831698,
                "UserComplainted": true,
                "ToEmailAddress": "example@cloud.com",
                "FromEmailAddress": "noreply@tencent.com",
                "UserClicked": true,
                "DeliverTime": 1609831698,
                "DeliverMessage": "",
                "MessageId": "qcloudses-30-4123414323-date-20210101094334-syNARhMTbKI1",
                "SendStatus": 0,
                "DeliverStatus": 0
            }
        ],
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72"
    }
}
```

