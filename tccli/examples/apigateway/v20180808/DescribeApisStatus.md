**Example 1: 查询API状态**

用于查看一个服务下的某个 API 或所有 API 列表及其相关信息。

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
            "TotalCount": 0,
            "ApiIdStatusSet": [
                {
                    "ServiceId": "abc",
                    "ApiId": "abc",
                    "ApiDesc": "abc",
                    "CreatedTime": "2020-09-22T00:00:00+00:00",
                    "ModifiedTime": "2020-09-22T00:00:00+00:00",
                    "ApiName": "abc",
                    "VpcId": 0,
                    "UniqVpcId": "abc",
                    "ApiType": "abc",
                    "Protocol": "abc",
                    "IsDebugAfterCharge": true,
                    "AuthType": "abc",
                    "ApiBusinessType": "abc",
                    "AuthRelationApiId": "abc",
                    "OauthConfig": {
                        "PublicKey": "abc",
                        "TokenLocation": "abc",
                        "LoginRedirectUrl": "abc"
                    },
                    "RelationBuniessApiIds": [
                        "abc"
                    ],
                    "Tags": [
                        {}
                    ],
                    "Path": "abc",
                    "Method": "abc"
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

