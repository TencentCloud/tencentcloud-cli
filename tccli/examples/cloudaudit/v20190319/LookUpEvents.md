**Example 1: 日志检索**

用于对操作日志进行检索，便于用户进行查询相关的操作信息。

Input: 

```
tccli cloudaudit LookUpEvents --cli-unfold-argument  \
    --EndTime 1553056687 \
    --LookupAttributes.0.AttributeKey AccessKeyId \
    --LookupAttributes.0.AttributeValue XXXX \
    --StartTime 1553056487
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "CloudAuditEvent": "{\"actionType\":\"Read\",\"apiErrorCode\":\"\",\"apiErrorMessage\":\"\",\"apiVersion\":\"2.0\",\"errorCode\":0,\"errorMessage\":\"permission verify\",\"eventID\":\"e92a92fc259c4a9333d2a7ce64d1ef201\",\"eventName\":\"LookupEvents\",\"eventRegion\":\"ap-guangzhou\",\"eventSource\":\"cloudaudit.api.tencentyun.com/v2/index.php\",\"eventTime\":\"2019-03-20 12:36:27\",\"eventType\":\"ConsoleCall\",\"eventVersion\":2,\"httpMethod\":\"POST\",\"region\":\"\",\"requestID\":\"15936031437374_1553056587.6815_v2\",\"requestParameters\":\"{\"Action\":\"LookupEvents\",\"EndTime\":\"1553097599\",\"MaxResults\":\"10\",\"Nonce\":\"36881\",\"Region\":\"gz\",\"RequestClient\":\"SDK_NODEJS_0.2.1\",\"RequestOperator\":\"1150691759\",\"RequestSource\":\"MC\",\"SecretId\":\"XXX\",\"StartTime\":\"1552406400\",\"Timestamp\":\"1553056583\",\"Token\":\"147d2c5b0319541a13d9fe6ceb5af2aae9b67f6610001\",\"seqId\":\"cdb9c38c-7031-bb13-6a9c-cd7641734c8f\"}\",\"resourceName\":\"\",\"resourceType\":\"cloudaudit\",\"resources\":\"\",\"sourceIPAddress\":\"59.37.125.124\",\"userAgent\":\"\",\"userIdentity\":{\"userName\":\"root\",\"type\":\"Root\",\"secretId\":\"XXX\",\"accountId\":1150691759,\"principalId\":1150691759,\"sessionContext\":{\"expireTime\":\"2019-03-20 13:04:46\",\"hasPolicyFilter\":0,\"extraInfo\":\"\",\"interfaceName\":\"\",\"ownerUin\":1150691759,\"ua\":\"27513f02ea3ab649f0cacb6476df54eb\",\"mfa\":0,\"userIp\":\"59.37.125.124\",\"mfaExpireTime\":\"2019-03-20 12:34:46\",\"uin\":1150691759,\"token\":\"147d2c5b0319541a13d9fe6ceb5af2aae9b67f6610001\",\"appId\":1251840716,\"policyFilter\":\"\"}}}",
                "EventId": "e92a92fc259c4a9333d2a7ce64d1ef201",
                "EventName": "LookupEvents",
                "EventTime": "2019-03-20 12:36:27",
                "SecretId": "XXX",
                "ErrorCode": 0,
                "RequestID": "15936031437374_1553056587.6815_v2",
                "AccountID": 1150691759,
                "SourceIPAddress": "59.37.125.124",
                "EventSource": "cloudaudit.api.tencentyun.com/v2/index.php",
                "EventRegion": "ap-guangzhou",
                "Resources": {
                    "ResourceName": "",
                    "ResourceType": "cloudaudit"
                },
                "Username": "root",
                "ResourceTypeCn": "云审计",
                "EventNameCn": "检索日志"
            }
        ],
        "NextToken": "DnF1ZXJ5VGhlbkZldGNoDwAAAAAAACBuFjNoRHJ5YTd4U1B5YWY4c1ZmMmxBQWcAAAAAAAAgnBZZZkZoYy04LVJJeVpJNnZJS2hIVTdRAAAAAAAAI1QWYk5mQmZXTzhTWXFNZjFMVlhHY1RjdwAAAAAAAB9sFmhZbV8xbm1FUXE2NGVDQndWSlNoMncAAAAAAAAd9BZOelN1aGMycFNydUVEQ0dQbzdCcEZBAAAAAAAALroWMTh4c00xalhRbk9wR0NsYWZvV20tQQAAAAAAACCdFllmRmhjLTgtUkl5Wkk2dklLaEhVN1EAAAAAAAAuuRYxOHhzTTFqWFFuT3BHQ2xhZm9XbS1BAAAAAAAAIJ4WWWZGaGMtOC1SSXlaSTZ2SUtoSFU3UQAAAAAAAB81FnN5aTBfTWJKU25HdXZuMWxsRkdJZ3cAAAAAAAApMhZ1UjdybjlCY1NRYUZVYWRub2x4YW9RAAAAAAAAHzQWc3lpMF9NYkpTbkd1dm4xbGxGR0lndwAAAAAAAB31Fk56U3VoYzJwU3J1RURDR1BvN0JwRkEAAAAAAAAfbRZoWW1fMW5tRVFxNjRlQ0J3VkpTaDJ3AAAAAAAAH24WaFltXzFubUVRcTY0ZUNCd1ZKU2gydw==",
        "ListOver": true,
        "RequestId": "91e2998d-edc0-4ba0-a76d-cebbbfd99391"
    }
}
```

