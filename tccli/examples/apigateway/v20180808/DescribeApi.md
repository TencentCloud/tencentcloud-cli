**Example 1: 查询API详情**



Input: 

```
tccli apigateway DescribeApi --cli-unfold-argument  \
    --ServiceId service-ody35h5e \
    --ApiId api-3v4tzy3u
```

Output: 
```
{
    "Response": {
        "Result": {
            "ServiceId": "service-ody35h5e",
            "ServiceName": "mytest",
            "ServiceDesc": "mytesttest",
            "ApiId": "api-3v4tzy3u",
            "ApiDesc": "get a user info",
            "CreatedTime": "2019-12-23T09:15:16Z",
            "ModifiedTime": "2020-02-22T02:05:29Z",
            "ApiName": "test1",
            "ApiType": "NORMAL",
            "Protocol": "HTTP",
            "AuthType": "NONE",
            "ApiBuniessType": "NORMAL",
            "AuthRelationApiId": "api-e92i2jds",
            "OauthConfig": null,
            "IsDebugAfterCharge": false,
            "RequestConfig": {
                "Path": "/users/{name}",
                "Method": "GET"
            },
            "ResponseType": "",
            "ResponseSuccessExample": "",
            "ResponseFailExample": "",
            "ResponseErrorCodes": [],
            "RequestParameters": [],
            "ServiceTimeout": 15,
            "ServiceType": "MOCK",
            "ServiceConfig": null,
            "ServiceParameters": null,
            "ConstantParameters": null,
            "ServiceMockReturnMessage": "Hello Serverless Framework.",
            "ServiceScfFunctionName": null,
            "ServiceScfFunctionNamespace": null,
            "ServiceScfFunctionQualifier": null,
            "ServiceScfIsIntegratedResponse": null,
            "ServiceWebsocketRegisterFunctionName": null,
            "ServiceWebsocketRegisterFunctionNamespace": null,
            "ServiceWebsocketRegisterFunctionQualifier": null,
            "ServiceWebsocketCleanupFunctionName": null,
            "ServiceWebsocketCleanupFunctionNamespace": null,
            "ServiceWebsocketCleanupFunctionQualifier": null,
            "InternalDomain": null,
            "ServiceWebsocketTransportFunctionName": null,
            "ServiceWebsocketTransportFunctionNamespace": null,
            "ServiceWebsocketTransportFunctionQualifier": null,
            "MicroServices": null,
            "MicroServicesInfo": null,
            "ServiceTsfLoadBalanceConf": null,
            "ServiceTsfHealthCheckConf": null,
            "AuthRequired": false,
            "EnableCORS": false,
            "Tags": []
        },
        "RequestId": "b1fb681f-fc43-41cc-a8bc-c3400270c2f9"
    }
}
```

