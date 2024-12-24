**Example 1: 查询微服务实例详情**



Input: 

```
tccli tsf DescribeMicroservice --cli-unfold-argument  \
    --MicroserviceId ms-a78gk87b \
    --Offset 0 \
    --Limit 10 \
    --GroupIds group-yx87px4a \
    --Filters.0.Name LanIp \
    --Filters.0.Values 172.16.16.139
```

Output: 
```
{
    "Response": {
        "RequestId": "80479d6c-27db-4d6c-b5f0-5ec576d2105f",
        "Result": {
            "Content": [
                {
                    "ApplicationId": "application-ydopqnxa",
                    "ApplicationName": "app-gw",
                    "ApplicationPackageVersion": "20241223011040",
                    "ApplicationType": "V",
                    "ClusterId": "cluster-2vz3nd3a",
                    "ClusterName": "cls_name",
                    "ClusterType": "V",
                    "GroupId": "group-yx87px4a",
                    "GroupName": "zuul-2",
                    "HealthCheckUrl": null,
                    "HiddenStatus": "unhidden",
                    "InstanceAvailableStatus": null,
                    "InstanceId": "ins-7wy598p8",
                    "InstanceName": "app22",
                    "InstanceStatus": null,
                    "LanIp": "172.16.16.139",
                    "LastHeartbeatTime": 1734943598,
                    "MetaJson": "H4sIAAAAAAAAAGXQUU+DMBQF4P/SZ7tAh2nxjUDHiFtpWmbiXki3EUaibdmGgsb/LpPOmPh8vntycj9BIRdlxPkqi6Miy1mZJeABKGtfmr26NEbD4WBsq3sF7n5sLOgEi2xNR+rjeUAIxgFxIBX5hk819cl0Fg49wbYPbgUZkwWLYjqRRp8hfh/uQ2JvBSxaU8l/hVav1dmqfQVbtcO7Nnz754pnfp2S0IWLuMjT8okKOQ4dA+ShwEdo7vm+F3jOCJpOqbKw7pSuP46mc5lMHv+c+zMUzpAHl6a/jA9ZNvWxOkFBVzSS1F1sc3adAL6+AZBHey5SAQAA",
                    "NamespaceId": null,
                    "NamespaceName": null,
                    "Port": "8080",
                    "RegistrationId": "ins-7wy598p8",
                    "RegistrationTime": 1734887748,
                    "ServiceInstanceStatus": "Running",
                    "ServiceStatus": "passing",
                    "WanIp": "43.139.245.156"
                }
            ],
            "TotalCount": 1
        }
    }
}
```

