**Example 1: 查询网关下分组和API**



Input: 

```
tccli tsf DescribeGatewayAllGroupApis --cli-unfold-argument  \
    --GatewayDeployGroupId group-yd3b588a \
    --SearchWord default
```

Output: 
```
{
    "Response": {
        "RequestId": "8d5aacf5-0ad5-40ed-85ca-d7ef71c85c57",
        "Result": {
            "GatewayDeployGroupId": "group-yd3b588a",
            "GatewayDeployGroupName": "group-zuul-1",
            "GroupNum": 1,
            "Groups": [
                {
                    "GatewayInstanceId": "gw-ins-b09khqjq",
                    "GatewayInstanceType": "none",
                    "GroupApiCount": 2,
                    "GroupApis": [
                        {
                            "ApiId": "api-0i1r0zuh",
                            "Method": "GET",
                            "MicroserviceName": "provider-demo",
                            "NamespaceName": "ns_default",
                            "Path": "/checkToken"
                        },
                        {
                            "ApiId": "api-m0csucjn",
                            "Method": "GET",
                            "MicroserviceName": "provider-demo",
                            "NamespaceName": "ns_default",
                            "Path": "/swagger/getMessageDetail"
                        }
                    ],
                    "GroupId": "grp-nb08ur29",
                    "GroupName": "grp_app"
                }
            ]
        }
    }
}
```

