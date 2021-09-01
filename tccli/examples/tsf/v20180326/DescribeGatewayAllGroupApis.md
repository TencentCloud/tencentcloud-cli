**Example 1: 查询网关下分组和API**



Input: 

```
tccli tsf DescribeGatewayAllGroupApis --cli-unfold-argument  \
    --GatewayDeployGroupId group-zbyxk4aa
```

Output: 
```
{
    "Response": {
        "RequestId": "0a1c8ed2-7a69-4a12-87f0-a6ca4b6419f8",
        "Result": {
            "GatewayDeployGroupId": "group-zbyxk4aa",
            "GatewayDeployGroupName": "sean-test",
            "GroupNum": 1,
            "Groups": [
                {
                    "GroupId": "grp-aocm2u1n",
                    "GroupName": "test",
                    "GroupApiCount": 3,
                    "GroupApis": [
                        {
                            "ApiId": "api-3bpjclfs",
                            "Path": "/v1/user/{userId}",
                            "Method": "POST",
                            "MicroserviceName": "provider-demo",
                            "NamespaceName": "test-ns2"
                        },
                        {
                            "ApiId": "api-5lf5r4i3",
                            "Path": "/v1/user/create/user",
                            "Method": "POST",
                            "MicroserviceName": "provider-demo",
                            "NamespaceName": "test-ns"
                        },
                        {
                            "ApiId": "api-3e1583de",
                            "Path": "/echo/{param}",
                            "Method": "GET",
                            "MicroserviceName": "provider-demo",
                            "NamespaceName": "test-ns"
                        }
                    ]
                }
            ]
        }
    }
}
```

