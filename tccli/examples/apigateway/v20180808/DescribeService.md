**Example 1: Querying service details**



Input: 

```
tccli apigateway DescribeService --cli-unfold-argument  \
    --ServiceId service-rypiqi13
```

Output: 
```
{
    "Response": {
        "ServiceId": "service-rypiqi13",
        "AvailableEnvironments": [
            "release"
        ],
        "ServiceName": "dd",
        "ServiceDesc": "",
        "Protocol": "http",
        "CreatedTime": "2020-04-15T11:03:41Z",
        "ModifiedTime": "2020-04-15T11:03:42Z",
        "ExclusiveSetName": "",
        "IpVersion": "IPv4",
        "UserType": "",
        "NetTypes": [
            "OUTER"
        ],
        "InternalSubDomain": "",
        "OuterSubDomain": "service-rypiqi13-1259027407.bj.apigw.tencentcs.com",
        "InnerHttpPort": 0,
        "InnerHttpsPort": 0,
        "SetId": 1,
        "ApiTotalCount": 1,
        "ApiIdStatusSet": [
            {
                "ServiceId": "service-rypiqi13",
                "ApiId": "api-mpnvjg0b",
                "ApiDesc": "",
                "Path": "/",
                "Method": "GET",
                "CreatedTime": "2020-05-18T11:11:04Z",
                "ModifiedTime": "2020-05-18T11:11:04Z",
                "ApiName": "test_tag",
                "UniqVpcId": "",
                "ApiType": "NORMAL",
                "Protocol": "HTTP",
                "IsDebugAfterCharge": false,
                "AuthType": "NONE",
                "ApiBusinessType": "NORMAL",
                "AuthRelationApiId": "",
                "OauthConfig": null,
                "TokenLocation": null,
                "RelationBuniessApiIds": null
            }
        ],
        "UsagePlanTotalCount": 0,
        "UsagePlanList": [],
        "RequestId": "b15e7661-c598-4747-85f9-44fc44118608"
    }
}
```

