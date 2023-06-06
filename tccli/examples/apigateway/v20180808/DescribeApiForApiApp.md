**Example 1: DescribeApiForApiApp**



Input: 

```
tccli apigateway DescribeApiForApiApp --cli-unfold-argument  \
    --ServiceId service-ody35h5e \
    --ApiId api-3v4tzy3u \
    --ApiRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "Result": {
            "EnableCORS": false,
            "ServiceDesc": "xx",
            "RequestParameters": [
                {
                    "Name": "xx",
                    "DefaultValue": "xx",
                    "Required": true,
                    "Position": "xx",
                    "Type": "xx",
                    "Desc": "xx"
                }
            ],
            "InternalDomain": "xx",
            "RequestConfig": {
                "Path": "xx",
                "Method": "xx"
            },
            "ServiceWebsocketRegisterFunctionQualifier": "xx",
            "MicroServices": [
                {
                    "MicroServiceName": "xx",
                    "ClusterId": "xx",
                    "NamespaceId": "xx"
                }
            ],
            "ServiceWebsocketRegisterFunctionNamespace": "xx",
            "CreatedTime": "2020-09-22T00:00:00+00:00",
            "ConstantParameters": [
                {
                    "Position": "xx",
                    "DefaultValue": "xx",
                    "Name": "xx",
                    "Desc": "xx"
                }
            ],
            "ServiceTsfLoadBalanceConf": {
                "SessionStickRequired": true,
                "IsLoadBalance": true,
                "SessionStickTimeout": 0,
                "Method": "xx"
            },
            "ServiceWebsocketTransportFunctionNamespace": "xx",
            "ServiceScfFunctionQualifier": "xx",
            "ServiceScfIsIntegratedResponse": true,
            "ServiceWebsocketTransportFunctionName": "xx",
            "ResponseSuccessExample": "xx",
            "ServiceConfig": {
                "Product": "xx",
                "UniqVpcId": "xx",
                "Url": "xx",
                "UpstreamId": "xx",
                "Path": "xx",
                "Method": "xx"
            },
            "Tags": [
                {
                    "Value": "xx",
                    "Key": "xx"
                }
            ],
            "ServiceParameters": [
                {
                    "RelevantRequestParameterPosition": "xx",
                    "Name": "xx",
                    "RelevantRequestParameterDesc": "xx",
                    "DefaultValue": "xx",
                    "RelevantRequestParameterName": "xx",
                    "Position": "xx"
                }
            ],
            "ServiceScfFunctionNamespace": "xx",
            "ServiceWebsocketRegisterFunctionName": "xx",
            "ServiceWebsocketTransportFunctionQualifier": "xx",
            "IsDebugAfterCharge": false,
            "ApiBusinessType": "xx",
            "ApiName": "xx",
            "Base64EncodedTriggerRules": [
                {
                    "Name": "xx",
                    "Value": [
                        "xx"
                    ]
                },
                {
                    "Name": "xx",
                    "Value": [
                        "xx"
                    ]
                }
            ],
            "ResponseFailExample": "xx",
            "ResponseType": "xx",
            "AuthType": "xx",
            "ServiceTimeout": 15,
            "ServiceName": "xx",
            "ApiDesc": "xx",
            "ServiceWebsocketCleanupFunctionQualifier": "xx",
            "OauthConfig": {
                "PublicKey": "xx",
                "LoginRedirectUrl": "xx",
                "TokenLocation": "xx"
            },
            "IsBase64Trigger": false,
            "ServiceScfFunctionName": "xx",
            "ServiceTsfHealthCheckConf": {
                "RequestVolumeThreshold": 0,
                "SleepWindowInMilliseconds": 0,
                "ErrorThresholdPercentage": 0,
                "IsHealthCheck": true
            },
            "ServiceMockReturnMessage": "xx",
            "ResponseErrorCodes": [
                {
                    "Msg": "xx",
                    "NeedConvert": true,
                    "Code": 0,
                    "ConvertedCode": 0,
                    "Desc": "xx"
                }
            ],
            "ServiceType": "xx",
            "AuthRelationApiId": "xx",
            "ModifiedTime": "2020-09-22T00:00:00+00:00",
            "MicroServicesInfo": [
                0
            ],
            "ApiId": "xx",
            "Environments": [
                "xx"
            ],
            "ApiType": "xx",
            "ServiceId": "xx",
            "ServiceWebsocketCleanupFunctionName": "xx",
            "Protocol": "xx",
            "IsBase64Encoded": false,
            "ServiceWebsocketCleanupFunctionNamespace": "xx"
        },
        "RequestId": "xx"
    }
}
```

