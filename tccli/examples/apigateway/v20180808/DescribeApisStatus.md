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
                    "ServiceId": "service-ody35h5e",
                    "ApiId": "api-k3ezsaoi",
                    "ApiDesc": "desc",
                    "Path": "/lkjdszfhbgv",
                    "Method": "GET",
                    "CreatedTime": "2020-02-28T11:26:33Z",
                    "ModifiedTime": "2020-02-28T11:26:33Z",
                    "ApiName": "name",
                    "VpcId": -1,
                    "UniqVpcId": "",
                    "ApiType": "NORMAL",
                    "Protocol": "HTTP",
                    "IsDebugAfterCharge": false,
                    "AuthType": "NONE",
                    "ApiBuniessType": "NORMAL",
                    "AuthRelationApiId": "",
                    "AuthRequired": true,
                    "OauthConfig": null,
                    "TokenLocation": null,
                    "RelationBuniessApiIds": null,
                    "Tags": []
                }
            ]
        },
        "RequestId": "d617a773-cfbd-47a7-8762-b213dcb681f0"
    }
}
```

