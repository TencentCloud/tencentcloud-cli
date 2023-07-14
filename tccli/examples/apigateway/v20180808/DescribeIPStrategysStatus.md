**Example 1: DescribeIPStrategysStatus**

用于查询服务IP策略列表，因为接口名拼写错误，已不推荐使用，请优先使用DescribeIPStrategiesStatus接口。

Input: 

```
tccli apigateway DescribeIPStrategysStatus --cli-unfold-argument  \
    --ServiceId service-ody35h5e
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 0,
            "StrategySet": [
                {
                    "StrategyId": "abc",
                    "StrategyName": "abc",
                    "StrategyType": "abc",
                    "StrategyData": "abc",
                    "CreatedTime": "2020-09-22T00:00:00+00:00",
                    "ModifiedTime": "2020-09-22T00:00:00+00:00",
                    "ServiceId": "abc",
                    "BindApiTotalCount": 0,
                    "BindApis": [
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
                                "abc"
                            ],
                            "Path": "abc",
                            "Method": "abc"
                        }
                    ]
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

