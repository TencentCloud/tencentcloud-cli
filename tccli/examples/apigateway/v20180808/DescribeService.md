**Example 1: 用于查询服务详情**

无

Input: 

```
tccli apigateway DescribeService --cli-unfold-argument  \
    --ServiceId service-rypiqi13
```

Output: 
```
{
    "Response": {
        "ServiceDesc": "sesrxx",
        "CreatedTime": "2020-09-22T00:00:00+00:00",
        "SetId": 1,
        "InnerHttpsPort": 0,
        "InnerHttpPort": 0,
        "UniqVpcId": "vpc-abc",
        "Tags": [
            {
                "Value": "test",
                "Key": "test"
            }
        ],
        "NetTypes": [
            "OUTER"
        ],
        "IpVersion": "",
        "UserType": "",
        "UsagePlanList": [
            {
                "MaxRequestNumPreSec": 0,
                "UsagePlanId": "",
                "ModifiedTime": "2020-09-22T00:00:00+00:00",
                "UsagePlanDesc": "test",
                "Environment": "test",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "UsagePlanName": "sdfafxx"
            }
        ],
        "OuterSubDomain": "domain.com",
        "UsagePlanTotalCount": 0,
        "SetType": "",
        "ApiIdStatusSet": [
            {
                "AuthType": "",
                "Protocol": "",
                "UniqVpcId": "",
                "ModifiedTime": "2020-09-22T00:00:00+00:00",
                "OauthConfig": {
                    "PublicKey": "",
                    "LoginRedirectUrl": "",
                    "TokenLocation": ""
                },
                "ApiId": "",
                "AuthRelationApiId": "",
                "ApiDesc": "",
                "ApiType": "",
                "ApiBusinessType": "",
                "ServiceId": "",
                "ApiName": "",
                "Path": "",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "RelationBuniessApiIds": [
                    ""
                ],
                "IsDebugAfterCharge": false,
                "Method": "",
                "TokenLocation": ""
            }
        ],
        "ServiceName": "",
        "RequestId": "",
        "InstanceName": "",
        "Protocol": "",
        "ApiTotalCount": 1,
        "ModifiedTime": "2020-09-22T00:00:00+00:00",
        "DeploymentType": "DEFAULT",
        "SpecialUse": "DEFAULT",
        "InstanceId": "",
        "AvailableEnvironments": [
            "release"
        ],
        "ServiceId": "",
        "InternalSubDomain": ""
    }
}
```

