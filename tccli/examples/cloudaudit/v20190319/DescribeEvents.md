**Example 1: 查询云审计日志**



Input: 

```
tccli cloudaudit DescribeEvents --cli-unfold-argument  \
    --StartTime 1610613170 \
    --EndTime 1610699570 \
    --MaxResults 1
```

Output: 
```
{
    "Response": {
        "ListOver": false,
        "Events": [
            {
                "CloudAuditEvent": "{\"userIdentity\":{\"principalId\":\"100000000000\",\"accountId\":\"100000000000\",\"secretId\":\"xxx\",\"type\":\"Root\",\"userName\":\"root\",\"sessionContext\":\"{\\\"token\\\": \\\"xxx\\\", \\\"userIp\\\": \\\"163.177.68.30\\\", \\\"uin\\\": 100000000000, \\\"ownerUin\\\": 100000000000, \\\"appId\\\": 1000000000, \\\"expireTime\\\": \\\"2021-01-15 17:35:55\\\", \\\"mfa\\\": 0, \\\"mfaExpireTime\\\": \\\"0000-00-00 00:00:00\\\", \\\"interfaceName\\\": \\\"\\\", \\\"hasPolicyFilter\\\": 0, \\\"policyFilter\\\": \\\"\\\", \\\"extraInfo\\\": \\\"\\\"}\"},\"@timestamp\":\"2021-01-15T07:35:59.115042\",\"onlyRecordNotSeen\":\"0\",\"eventRegion\":\"ap-guangzhou\",\"eventVersion\":2,\"errorCode\":\"0\",\"errorMessage\":\"permission verify\",\"requestID\":\"c8c04477-eb9e-4703-84ae-f8758c6084ff\",\"eventID\":\"c8c04477-eb9e-4703-84ae-f8758c6084ff\",\"apiVersion\":\"3.0\",\"eventType\":\"ConsoleCall\",\"actionType\":\"Read\",\"authMode\":\"0\",\"isRisk\":\"0\",\"ruleId\":\"0\",\"httpMethod\":\"POST\",\"apiErrorCode\":\"0\",\"apiErrorMessage\":\"\",\"userAgent\":\"SDK_NODEJS_0.2.1\",\"eventTime\":1610696155,\"updateEsTime\":16106961641644206,\"sensitiveAction\":\"\",\"eventPlatform\":\"0\",\"sourceIPAddress\":\"9.83.55.32\",\"resourceType\":\"cloudaudit\",\"eventName\":\"LookUpEvents\",\"eventSource\":\"cloudaudit.ap-chongqing.api.tencentyun.com\",\"requestParameters\":\"{\\\"Region\\\": \\\"ap-guangzhou\\\", \\\"SecretId\\\": \\\"xxx\\\", \\\"Timestamp\\\": \\\"1610696155\\\", \\\"Nonce\\\": \\\"11289\\\", \\\"RequestClient\\\": \\\"SDK_NODEJS_0.2.1\\\", \\\"StartTime\\\": \\\"1610121600\\\", \\\"EndTime\\\": \\\"1610726399\\\", \\\"MaxResults\\\": \\\"20\\\", \\\"Mode\\\": \\\"standard\\\", \\\"Version\\\": \\\"2019-03-19\\\", \\\"Action\\\": \\\"LookUpEvents\\\", \\\"RequestOperator\\\": \\\"100000000000\\\", \\\"Token\\\": \\\"xxx\\\", \\\"RequestSource\\\": \\\"MC\\\", \\\"seqId\\\": \\\"1be35142-f784-64d4-4502-a1250702edcd\\\"}\",\"resources\":\"[\\\"*\\\"]\",\"resourceName\":\"\",\"cloudapi\":1,\"auth\":1,\"signature\":0}",
                "EventName": "LookUpEvents",
                "EventTime": 1610696155,
                "SecretId": "xxx",
                "ErrorCode": "0",
                "RequestID": "c8c04477-eb9e-4703-84ae-f8758c6084ff",
                "SourceIPAddress": "9.83.55.32",
                "EventSource": "cloudaudit.ap-chongqing.api.tencentyun.com",
                "EventRegion": "ap-guangzhou",
                "Resources": {
                    "ResourceName": "",
                    "ResourceType": "cloudaudit"
                },
                "Username": "root",
                "ResourceTypeCn": "云审计",
                "EventNameCn": "",
                "ResourceRegion": ""
            }
        ],
        "NextToken": 16106961641644206,
        "RequestId": "2d4a7fba-bba8-452e-a99e-ccf11fdaa583"
    }
}
```

