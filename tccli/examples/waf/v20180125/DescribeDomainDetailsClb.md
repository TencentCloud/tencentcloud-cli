**Example 1: 查询单个clbwaf域名详情**



Input: 

```
tccli waf DescribeDomainDetailsClb --cli-unfold-argument  \
    --Domain lucasssli3.qcloud.com \
    --DomainId 20200728142847163546341 \
    --InstanceId waf_000000002
```

Output: 
```
{
    "Response": {
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2",
        "DomainsClbPartInfo": {
            "Domain": "pea.qcloudwaf.com",
            "DomainId": "waf-xOmbLKVc",
            "InstanceId": "waf_0000001ll",
            "Edition": "clb-waf",
            "InstanceName": "3211111",
            "IsCdn": 1,
            "FlowMode": 1,
            "LoadBalancerSet": [
                {
                    "ListenerId": "lbl-p08ll1la",
                    "ListenerName": "pea.qcloudwaf.com",
                    "LoadBalancerId": "lb-azo6s2m8",
                    "LoadBalancerName": "lb-6017c5bd",
                    "Protocol": "HTTP",
                    "Region": "gz",
                    "Vip": "203.195.250.6",
                    "Vport": 5803,
                    "Zone": "",
                    "NumericalVpcId": 0,
                    "LoadBalancerType": "abc"
                }
            ],
            "State": 0,
            "AlbType": "abc",
            "IpHeaders": [
                "abc"
            ],
            "CdcClusters": "abc"
        }
    }
}
```

