**Example 1: 查询单个clbwaf域名详情**



Input: 

```
tccli waf DescribeDomainDetailsClb --cli-unfold-argument  \
    --Domain lucasssli3.qcloudwaf.com \
    --DomainId waf-xOmbLKVc \
    --InstanceId waf_00vsdfgh1232
```

Output: 
```
{
    "Response": {
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2",
        "DomainsClbPartInfo": {
            "Domain": "lucasssli3.qcloudwaf.com",
            "DomainId": "waf-xOmbLKVc",
            "InstanceId": "waf_2kuil1fxvsfm7z3",
            "Edition": "clb-waf",
            "InstanceName": "gz-Default1",
            "IsCdn": 1,
            "FlowMode": 1,
            "LoadBalancerSet": [
                {
                    "ListenerId": "lbl-p08ll1la",
                    "ListenerName": "http-80",
                    "LoadBalancerId": "lb-azo6s2m8",
                    "LoadBalancerName": "lb-6017c5bd",
                    "Protocol": "HTTP",
                    "Region": "gz",
                    "Vip": "203.195.250.6",
                    "Vport": 5803,
                    "NumericalVpcId": 0,
                    "LoadBalancerType": "OPEN"
                }
            ],
            "State": 0,
            "AlbType": "clb",
            "IpHeaders": [
                "1.1.2.4"
            ],
            "CdcClusters": "cluster-asd"
        }
    }
}
```

