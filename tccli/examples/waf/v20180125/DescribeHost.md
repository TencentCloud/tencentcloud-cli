**Example 1: 获取防护域名详情**



Input: 

```
tccli waf DescribeHost --cli-unfold-argument  \
    --InstanceID waf_in3adnjuasrg \
    --Domain test.qcloudwaf.com \
    --DomainId dasfiheigo873uhf8e390fds93
```

Output: 
```
{
    "Response": {
        "Host": {
            "Domain": "txcloudwaf.qcloudwaf.com",
            "DomainId": "waf-DhOzNw3D",
            "MainDomain": "qcloudwaf.com",
            "Mode": 1,
            "Status": 1,
            "State": 1,
            "Engine": 1,
            "IsCdn": 1,
            "LoadBalancerSet": [
                {
                    "LoadBalancerId": "lb-daiu3grtd",
                    "LoadBalancerName": "txlb",
                    "ListenerId": "lbl-daskhe2",
                    "ListenerName": "80httpport",
                    "Vip": "35.68.12.3",
                    "Vport": 1,
                    "Region": "gz",
                    "Protocol": "http",
                    "Zone": "ap-guangzhou",
                    "NumericalVpcId": 3243,
                    "LoadBalancerType": "open"
                }
            ],
            "Region": "gz",
            "Edition": "clb-waf",
            "FlowMode": 1,
            "ClsStatus": 1,
            "Level": 1,
            "CdcClusters": [
                "cluster-o41khj88"
            ],
            "AlbType": "clb",
            "IpHeaders": [
                "x-myreal-ip"
            ],
            "EngineType": 0,
            "CloudType": "public",
            "Note": "备注"
        },
        "RequestId": "0ed6569e-f9b5-418d-8338-63eda4f2c0f7"
    }
}
```

