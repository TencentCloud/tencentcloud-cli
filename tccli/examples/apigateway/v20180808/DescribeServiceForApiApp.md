**Example 1: DescribeServiceForApiApp**

应用使用者查询服务详情

Input: 

```
tccli apigateway DescribeServiceForApiApp --cli-unfold-argument  \
    --ServiceId service-rypiqi13 \
    --ApiRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "ServiceId": "abc",
        "AvailableEnvironments": [
            "abc"
        ],
        "ServiceName": "abc",
        "ServiceDesc": "abc",
        "Protocol": "abc",
        "CreatedTime": "2020-09-22T00:00:00+00:00",
        "ModifiedTime": "2020-09-22T00:00:00+00:00",
        "NetTypes": [
            "abc"
        ],
        "InternalSubDomain": "abc",
        "OuterSubDomain": "abc",
        "InnerHttpPort": 0,
        "InnerHttpsPort": 0,
        "ApiTotalCount": 0,
        "ApiIdStatusSet": [
            {
                "ServiceId": "abc",
                "ApiId": "abc",
                "ApiDesc": "abc",
                "Path": "abc",
                "Method": "abc",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "ModifiedTime": "2020-09-22T00:00:00+00:00",
                "ApiName": "abc",
                "UniqVpcId": "abc",
                "ApiType": "abc",
                "Protocol": "abc",
                "IsDebugAfterCharge": true,
                "AuthType": "abc",
                "ApiBusinessType": "abc",
                "AuthRelationApiId": "abc",
                "RelationBuniessApiIds": [
                    "abc"
                ],
                "OauthConfig": {
                    "PublicKey": "abc",
                    "TokenLocation": "abc",
                    "LoginRedirectUrl": "abc"
                },
                "TokenLocation": "abc"
            }
        ],
        "UsagePlanTotalCount": 0,
        "UsagePlanList": [
            {
                "Environment": "abc",
                "UsagePlanId": "abc",
                "UsagePlanName": "abc",
                "UsagePlanDesc": "abc",
                "MaxRequestNumPreSec": 0,
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "ModifiedTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "IpVersion": "abc",
        "UserType": "abc",
        "SetId": 0,
        "Tags": [
            {
                "Key": "abc",
                "Value": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

