**Example 1: 查询API状态**



Input: 

```
tccli apigateway DescribeApisStatus --cli-unfold-argument  \
    --ServiceId service-ody35h5e
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "ApiIdStatusSet": [
                {
                    "RelationBuniessApiIds": [
                        "xx"
                    ],
                    "CreatedTime": "2020-09-22T00:00:00+00:00",
                    "Method": "xx",
                    "VpcId": 0,
                    "Tags": [
                        "xx"
                    ],
                    "IsDebugAfterCharge": false,
                    "ApiBusinessType": "xx",
                    "ApiName": "xx",
                    "Path": "xx",
                    "AuthType": "xx",
                    "ApiDesc": "xx",
                    "OauthConfig": {
                        "PublicKey": "xx",
                        "LoginRedirectUrl": "xx",
                        "TokenLocation": "xx"
                    },
                    "AuthRelationApiId": "xx",
                    "Protocol": "xx",
                    "ModifiedTime": "2020-09-22T00:00:00+00:00",
                    "UniqVpcId": "xx",
                    "ApiId": "xx",
                    "ApiType": "xx",
                    "ServiceId": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

