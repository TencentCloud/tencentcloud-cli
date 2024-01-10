**Example 1: 查询操作审计日志**

查询操作审计日志

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
        "ListOver": true,
        "Events": [
            {
                "CloudAuditEvent": "{\"userIdentity\":{\"principalId\":\"1000000000\",\"accountId\":\"1000000000\",\"secretId\":\"xxx\",\"sessionContext\":\"{\\\"token\\\": \\\"xxx--Jqr7dXvw3EBEXWNcJljzbZeJeoIrQx9gafWtHV1Lg9zu7hSpY91LAF414n21D41bpodncbz8u12C-xxx\\\", \\\"ua\\\": \\\"xxx\\\", \\\"userIp\\\": \\\"111.111.11.111\\\", \\\"uin\\\": 1000000000, \\\"ownerUin\\\": 1000000000, \\\"appId\\\": 1256196555, \\\"expireTime\\\": \\\"2023-04-03 19:23:29\\\", \\\"mfa\\\": 1, \\\"mfaExpireTime\\\": \\\"0000-00-00 00:00:00\\\", \\\"interfaceName\\\": \\\"\\\", \\\"hasPolicyFilter\\\": 0, \\\"policyFilter\\\": \\\"\\\", \\\"extraInfo\\\": \\\"{\\\\\\\"dictId\\\\\\\":2208,\\\\\\\"mfaExpireTime\\\\\\\":\\\\\\\"3000-12-12 00:00:00\\\\\\\",\\\\\\\"sessionUin\\\\\\\":5000}\\\"}\",\"type\":\"Root\",\"userName\":\"root\"},\"eventRegion\":\"ap-guangzhou\",\"eventVersion\":2,\"errorCode\":\"0\",\"errorMessage\":\"\",\"requestID\":\"008ef803-4549-41fe-a7e6-433122273683\",\"eventID\":\"008ef803-4549-41fe-a7e6-433122273683\",\"apiVersion\":\"3.0\",\"eventType\":\"ConsoleCall\",\"actionType\":\"Write\",\"httpMethod\":\"POST\",\"apiErrorCode\":0,\"apiErrorMessage\":\"\",\"userAgent\":\"SDK_NODEJS_0.2.1\",\"eventTime\":1680513809,\"sourceIPAddress\":\"111.111.111.111\",\"eventSource\":\"cloudaudit.ap-guangzhou.api.tencentyun.com\",\"resources\":\"[\\\"*\\\"]\",\"resourceName\":\"\",\"resourceSet\":[],\"requestParameters\":\"{\\\"ActionType\\\":\\\"Write\\\",\\\"EventNames\\\":[\\\"*\\\"],\\\"Name\\\":\\\"qweqwe\\\",\\\"ResourceType\\\":\\\"*\\\",\\\"Status\\\":1,\\\"Storage\\\":{\\\"StorageName\\\":\\\"d0f00ec9-5643-4a11-9022-187621d38714\\\",\\\"StoragePrefix\\\":\\\"cloudaudit\\\",\\\"StorageRegion\\\":\\\"ap-guangzhou\\\",\\\"StorageType\\\":\\\"cls\\\"},\\\"Version\\\":\\\"2019-03-19\\\"}\",\"responseElements\":\"{\\\"TrackId\\\":21915,\\\"RequestId\\\":\\\"008ef803-4549-41fe-a7e6-433122273683\\\"}\",\"resourceType\":\"cloudaudit\",\"eventName\":\"CreateAuditTrack\",\"sensitiveAction\":\"1\",\"tags\":[\"\"]}",
                "EventName": "CreateAuditTrack",
                "EventTime": "1680513809",
                "SecretId": "xxxxxxx",
                "ErrorCode": 0,
                "RequestID": "008ef803-4549-41fe-a7e6-433122273683",
                "SourceIPAddress": "111.111.111.111",
                "EventSource": "cloudaudit.ap-guangzhou.api.tencentyun.com",
                "EventRegion": "ap-guangzhou",
                "Resources": {
                    "ResourceName": "",
                    "ResourceType": "cloudaudit"
                },
                "Username": "root",
                "AccountID": 100004293724,
                "Location": "中国 广东省 深圳市 中国电信",
                "ResourceTypeCn": "云审计",
                "EventNameCn": "创建云审计跟踪集",
                "ResourceRegion": ""
            }
        ],
        "TotalCount": 1,
        "NextToken": 16805138109322956,
        "RequestId": "42a0e189-2869-488f-aa34-8bffd0814322"
    }
}
```

