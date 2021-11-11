**Example 1: DescribeMeshList**



Input: 

```
tccli tcm DescribeMeshList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397",
        "MeshList": [
            {
                "MeshId": "xxxxx",
                "DisplayName": "test",
                "Region": "xx",
                "Type": "HOSTED",
                "State": "xx",
                "Version": "xx",
                "CreatedTime": "2020-09-22 00:00:00",
                "UpdatedTime": "2020-09-22 00:00:00",
                "Config": {
                    "Istio": {
                        "OutboundTrafficPolicy": "ALLOW_ANY",
                        "Tracing": {
                            "Sampling": 1
                        }
                    }
                },
                "ClusterList": [
                    {
                        "ClusterId": "{{clusterId}}",
                        "DisplayName": "",
                        "Region": "sh",
                        "Role": "MASTER",
                        "VpcId": "{{vpcId}}",
                        "SubnetId": "{{subnetId}}",
                        "Config": {
                            "AutoInjectionNamespaceList": [
                                "default"
                            ]
                        }
                    }
                ],
                "Status": {
                    "CanaryVersion": "xx",
                    "ServiceCount": 0,
                    "Prometheus": null
                }
            }
        ],
        "Total": 1
    }
}
```

