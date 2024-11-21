**Example 1: 获取防护域名列表**



Input: 

```
tccli waf DescribeHosts --cli-unfold-argument  \
    --Domain txwaf.qcloudwaf.com \
    --DomainId waf-u23yt9Hj \
    --Search txwaf \
    --InstanceID waf_uadhiu2ads44a
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "HostList": [
            {
                "Domain": "txwaf.qcloudwaf.com",
                "DomainId": "waf-u23yt9Hj",
                "MainDomain": "qcloudwaf.com",
                "Mode": 1,
                "Status": 1,
                "State": 1,
                "Engine": 1,
                "IsCdn": 1,
                "LoadBalancerSet": [
                    {
                        "LoadBalancerId": "lb-ads3adsa",
                        "LoadBalancerName": "80http",
                        "ListenerId": "lbl-das32q",
                        "ListenerName": "80http",
                        "Vip": "23.25.123.23",
                        "Vport": 1,
                        "Region": "gz",
                        "Protocol": "http",
                        "Zone": "ap-guangzhou",
                        "NumericalVpcId": 54352,
                        "LoadBalancerType": "open"
                    }
                ],
                "Region": "gz",
                "Edition": "clb-waf",
                "FlowMode": 1,
                "ClsStatus": 1,
                "Level": 1,
                "CdcClusters": [],
                "AlbType": "clb",
                "IpHeaders": [
                    "x-real-ip"
                ],
                "EngineType": 0,
                "CloudType": "public",
                "Note": "备注"
            }
        ],
        "RequestId": "304cb36f-772a-4fdb-9b25-212d8fe5a553"
    }
}
```

