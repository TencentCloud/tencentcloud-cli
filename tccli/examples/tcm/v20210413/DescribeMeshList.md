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
                "Region": "sh",
                "Type": "HOSTED",
                "State": "pending",
                "Version": "1.12.5",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "UpdatedTime": "2020-09-22T00:00:00+00:00",
                "Config": {
                    "Istio": {
                        "OutboundTrafficPolicy": "ALLOW_ANY",
                        "Tracing": {
                            "Sampling": 1
                        },
                        "DisablePolicyChecks": true,
                        "EnablePilotHTTP": true,
                        "DisableHTTPRetry": true,
                        "SmartDNS": {
                            "IstioMetaDNSCapture": true,
                            "IstioMetaDNSAutoAllocate": true
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
                        "State": "RUNNING",
                        "HostedNamespaces": [],
                        "Type": "TKE",
                        "LinkedTime": "2020-09-22T00:00:00+00:00",
                        "Config": {
                            "AutoInjectionNamespaceList": [
                                "default"
                            ]
                        },
                        "Status": {
                            "LinkState": "LINKED",
                            "LinkErrorDetail": ""
                        }
                    }
                ],
                "Status": {
                    "CanaryVersion": "1.14.5",
                    "ServiceCount": 0,
                    "Prometheus": null
                },
                "TagList": [
                    {
                        "Key": "abc",
                        "Value": "abc",
                        "Passthrough": true
                    }
                ]
            }
        ],
        "Total": 1
    }
}
```

