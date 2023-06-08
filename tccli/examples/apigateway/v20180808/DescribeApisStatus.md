**Example 1: 查询API状态**

查询API状态

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
                        "123"
                    ],
                    "CreatedTime": "2020-09-22T00:00:00+00:00",
                    "Method": "123",
                    "VpcId": 0,
                    "Tags": [
                        "123"
                    ],
                    "IsDebugAfterCharge": false,
                    "ApiBusinessType": "1",
                    "ApiName": "1",
                    "Path": "1",
                    "AuthType": "1",
                    "ApiDesc": "1",
                    "OauthConfig": {
                        "PublicKey": "1",
                        "LoginRedirectUrl": "1",
                        "TokenLocation": "1"
                    },
                    "AuthRelationApiId": "1",
                    "Protocol": "1",
                    "ModifiedTime": "2020-09-22T00:00:00+00:00",
                    "UniqVpcId": "1",
                    "ApiId": "1",
                    "ApiType": "1",
                    "ServiceId": "1"
                }
            ]
        },
        "RequestId": "1"
    }
}
```

