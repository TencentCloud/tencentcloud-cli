**Example 1: 查询上下车点转发资源**



Input: 

```
tccli ga2 DescribeAcceleratorResourceDetail --cli-unfold-argument  \
    --GlobalAcceleratorId ga-8sreohed
```

Output: 
```
{
    "Response": {
        "AcceleratorResourceDetail": [
            {
                "EgressNodeList": [
                    {
                        "CloudType": "TENCENT",
                        "ClusterId": "gapclu-6fqmu5b4",
                        "ClusterName": "ap-guangzhou_pre_site-1",
                        "ClusterRegion": "ap-guangzhou",
                        "GaproxyListenerIpDetailList": [
                            {
                                "ForwardIp": "10.10.4.180",
                                "HostIp": "10.10.0.13",
                                "InstanceId": "ins-81kp202o",
                                "Port": 1621,
                                "PublicIp": ""
                            }
                        ],
                        "GaproxyListenerIpList": [
                            "10.10.4.180:1621"
                        ],
                        "GaproxyPortId": "gappt-ox7szprg",
                        "GaproxyProtocol": "TCP",
                        "GaproxyUpstreamList": [
                            {
                                "EndpointGroupId": "epg-5xdf29u9",
                                "GaproxyActionId": "gapac-plnbtsy4",
                                "GaproxyLocation": "/",
                                "GaproxyLocationId": "gaplo-qu8uc5rq",
                                "GaproxyServerId": "gapsvr-pprynb1g",
                                "GaproxyUpstreamId": "gapu-8r3jnw6p",
                                "OriginRegion": "ap-guangzhou",
                                "ProxyBindIpDetailList": [
                                    {
                                        "ForwardIp": "10.10.4.254",
                                        "HostIp": "10.10.0.13",
                                        "InstanceId": "ins-81kp202o",
                                        "PublicIp": "114.132.173.149"
                                    }
                                ],
                                "UpstreamServerList": [
                                    "12.13.12.12:80"
                                ]
                            }
                        ],
                        "ListenerId": "lsr-0oa2yohs",
                        "ListenerPort": 1621,
                        "ListenerProtocol": "TCP",
                        "Region": "ap-guangzhou"
                    }
                ],
                "EipList": [
                    {
                        "EipId": "eip-5z95ot65",
                        "LbId": "lb-gt18hb71",
                        "PublicIp": "152.136.178.143",
                        "Region": "ap-beijing"
                    }
                ],
                "GlobalAcceleratorId": "ga-8sreohed",
                "IngressNodeList": [
                    {
                        "CloudType": "TENCENT",
                        "ClusterId": "gapclu-3y1yfhxo",
                        "ClusterName": "ap-beijing_pre_site-1",
                        "ClusterRegion": "ap-beijing",
                        "GaproxyListenerIpDetailList": [
                            {
                                "ForwardIp": "10.13.37.103",
                                "HostIp": "10.13.32.16",
                                "InstanceId": "ins-m1hvvnr9",
                                "Port": 1127,
                                "PublicIp": ""
                            }
                        ],
                        "GaproxyListenerIpList": [
                            "10.13.37.103:1127"
                        ],
                        "GaproxyPortId": "gappt-235yjf7w",
                        "GaproxyProtocol": "TCP",
                        "GaproxyUpstreamList": [
                            {
                                "EndpointGroupId": "",
                                "GaproxyActionId": "gapac-1epueqyo",
                                "GaproxyLocation": "/",
                                "GaproxyLocationId": "gaplo-b1r1fn6e",
                                "GaproxyServerId": "gapsvr-gbd850f8",
                                "GaproxyUpstreamId": "gapu-fnjq7rln",
                                "OriginRegion": "ap-guangzhou",
                                "ProxyBindIpDetailList": [
                                    {
                                        "ForwardIp": "10.13.37.114",
                                        "HostIp": "10.13.32.16",
                                        "InstanceId": "ins-m1hvvnr9",
                                        "PublicIp": "152.136.199.72"
                                    }
                                ],
                                "UpstreamServerList": [
                                    "10.10.4.180:1621"
                                ]
                            }
                        ],
                        "ListenerId": "lsr-0oa2yohs",
                        "ListenerPort": 80,
                        "ListenerProtocol": "TCP",
                        "Region": "ap-beijing"
                    }
                ]
            }
        ],
        "RequestId": "72c81888-f330-422e-8652-9cf8b40eea2a"
    }
}
```

