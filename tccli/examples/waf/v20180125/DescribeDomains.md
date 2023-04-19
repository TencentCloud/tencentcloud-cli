**Example 1: 查询用户所有实例的详细信息**

查询用户所有实例的详细信息

Input: 

```
tccli waf DescribeDomains --cli-unfold-argument  \
    --Offset 1 \
    --Limit 20 \
    --Filters.0.Name Edition \
    --Filters.0.Values sparta_waf \
    --Filters.0.ExactMatch True \
    --Filters.1.Name InstanceId \
    --Filters.1.Values waf_000000002 \
    --Filters.1.ExactMatch True
```

Output: 
```
{
    "Response": {
        "RequestId": "b4f13899-561b-46a0-a045-6ba6b72c38f2",
        "Total": 8,
        "Domains": [
            {
                "AppId": 251000001,
                "Domain": "lsd-dev.qcloudwaf.com",
                "DomainId": "2020052111335540906556",
                "InstanceId": "waf_000000002",
                "InstanceName": "北京主实例",
                "State": 0,
                "Edition": "sparta-waf",
                "Region": "bj",
                "Cname": "bbde12a0caf91cac6a92d73b8674423e.qcloudwaf.com",
                "ClsStatus": 0,
                "FlowMode": 0,
                "Status": 1,
                "Mode": 1,
                "Engine": 1,
                "RsList": [
                    "118.24.149.159",
                    "118.24.0.195",
                    "118.24.40.208",
                    "118.24.63.83",
                    "118.24.46.247",
                    "119.27.186.134",
                    "118.24.140.18",
                    "118.24.97.152"
                ],
                "CCList": [],
                "Ports": [
                    {
                        "NginxServerId": 0,
                        "Port": "",
                        "Protocol": "",
                        "UpstreamPort": "",
                        "UpstreamProtocol": ""
                    }
                ],
                "LoadBalancerSet": []
            },
            {
                "AppId": 251000001,
                "Domain": "lsd.qcloud.com",
                "DomainId": "2020052111273557445011",
                "InstanceId": "waf_000000002",
                "InstanceName": "北京主实例",
                "State": 0,
                "Edition": "sparta-waf",
                "Region": "bj",
                "Cname": "a23dd45c10d76105479fe45df45e2e8a.qcloudwaf.com",
                "ClsStatus": 0,
                "FlowMode": 0,
                "Status": 1,
                "Mode": 1,
                "Engine": 22,
                "RsList": [
                    "118.24.149.159",
                    "118.24.0.195",
                    "118.24.40.208",
                    "118.24.63.83",
                    "118.24.46.247",
                    "119.27.186.134",
                    "118.24.140.18",
                    "118.24.97.152"
                ],
                "CCList": [],
                "Ports": [
                    {
                        "NginxServerId": 0,
                        "Port": "",
                        "Protocol": "",
                        "UpstreamPort": "",
                        "UpstreamProtocol": ""
                    }
                ],
                "LoadBalancerSet": []
            },
            {
                "AppId": 251000001,
                "Domain": "lucasssli4.qcloud.com",
                "DomainId": "2020052110473970432637",
                "InstanceId": "waf_000000002",
                "InstanceName": "北京主实例",
                "State": 0,
                "Edition": "sparta-waf",
                "Region": "bj",
                "Cname": "b089a068c570a4332ce1f749004ef528.qcloudwaf.com",
                "ClsStatus": 1,
                "FlowMode": 0,
                "Status": 1,
                "Mode": 0,
                "Engine": 10,
                "RsList": [
                    "118.24.149.159",
                    "118.24.0.195",
                    "118.24.40.208",
                    "118.24.63.83",
                    "118.24.46.247",
                    "119.27.186.134",
                    "118.24.140.18",
                    "118.24.97.152"
                ],
                "CCList": [],
                "Ports": [
                    {
                        "NginxServerId": 0,
                        "Port": "",
                        "Protocol": "",
                        "UpstreamPort": "",
                        "UpstreamProtocol": ""
                    }
                ],
                "LoadBalancerSet": []
            },
            {
                "AppId": 251000001,
                "Domain": "lucasssli3.qcloud.com",
                "DomainId": "20200728142847163546341",
                "InstanceId": "waf_000000002",
                "InstanceName": "北京主实例",
                "State": 0,
                "Edition": "sparta-waf",
                "Region": "bj",
                "Cname": "3ad9cafd1e917ab6d9e8c83dd9f31daf.qcloudwaf.com",
                "ClsStatus": 1,
                "FlowMode": 0,
                "Status": 1,
                "Mode": 1,
                "Engine": 20,
                "RsList": [
                    "118.24.149.159",
                    "118.24.0.195",
                    "118.24.40.208",
                    "118.24.63.83",
                    "118.24.46.247",
                    "119.27.186.134",
                    "118.24.140.18",
                    "118.24.97.152"
                ],
                "CCList": [],
                "Ports": [
                    {
                        "NginxServerId": 0,
                        "Port": "",
                        "Protocol": "",
                        "UpstreamPort": "",
                        "UpstreamProtocol": ""
                    }
                ],
                "LoadBalancerSet": []
            },
            {
                "AppId": 251000001,
                "Domain": "www.atestwaf.com",
                "DomainId": "waf-EYzKCNuq",
                "InstanceId": "waf_000000001",
                "InstanceName": "广州主实例",
                "State": 0,
                "Edition": "cdn-waf",
                "Region": "gz",
                "Cname": "",
                "ClsStatus": 0,
                "FlowMode": 0,
                "Status": 1,
                "Mode": 0,
                "Engine": 10,
                "RsList": [],
                "CCList": [],
                "Ports": [
                    {
                        "NginxServerId": 0,
                        "Port": "",
                        "Protocol": "",
                        "UpstreamPort": "",
                        "UpstreamProtocol": ""
                    }
                ],
                "LoadBalancerSet": [
                    {
                        "ListenerId": "",
                        "ListenerName": "",
                        "LoadBalancerId": "",
                        "LoadBalancerName": "",
                        "Protocol": "",
                        "Region": "",
                        "Vip": "",
                        "Vport": 0,
                        "Zone": ""
                    }
                ]
            },
            {
                "AppId": 251000001,
                "Domain": "www.testwaf.com",
                "DomainId": "waf-Ys4OU3yP",
                "InstanceId": "waf_000000001",
                "InstanceName": "广州主实例",
                "State": 0,
                "Edition": "cdn-waf",
                "Region": "gz",
                "Cname": "",
                "ClsStatus": 0,
                "FlowMode": 0,
                "Status": 1,
                "Mode": 0,
                "Engine": 10,
                "RsList": [],
                "CCList": [],
                "Ports": [
                    {
                        "NginxServerId": 0,
                        "Port": "",
                        "Protocol": "",
                        "UpstreamPort": "",
                        "UpstreamProtocol": ""
                    }
                ],
                "LoadBalancerSet": [
                    {
                        "ListenerId": "",
                        "ListenerName": "",
                        "LoadBalancerId": "",
                        "LoadBalancerName": "",
                        "Protocol": "",
                        "Region": "",
                        "Vip": "",
                        "Vport": 0,
                        "Zone": ""
                    }
                ]
            },
            {
                "AppId": 251000001,
                "Domain": "zc-clbbot.qcloudwaf.com",
                "DomainId": "waf-KdbeJVa6",
                "InstanceId": "waf_000000001",
                "InstanceName": "广州主实例",
                "State": 0,
                "Edition": "clb-waf",
                "Region": "gz",
                "Cname": "",
                "ClsStatus": 1,
                "FlowMode": 0,
                "Status": 1,
                "Mode": 0,
                "Engine": 20,
                "RsList": [],
                "CCList": [],
                "Ports": [
                    {
                        "NginxServerId": 0,
                        "Port": "",
                        "Protocol": "",
                        "UpstreamPort": "",
                        "UpstreamProtocol": ""
                    }
                ],
                "LoadBalancerSet": [
                    {
                        "ListenerId": "",
                        "ListenerName": "",
                        "LoadBalancerId": "",
                        "LoadBalancerName": "",
                        "Protocol": "",
                        "Region": "",
                        "Vip": "",
                        "Vport": 0,
                        "Zone": ""
                    }
                ]
            },
            {
                "AppId": 251000001,
                "Domain": "ipv6.qcloudwaf.com",
                "DomainId": "waf-0xGTMwMv",
                "InstanceId": "waf_000000001",
                "InstanceName": "广州主实例",
                "State": 0,
                "Edition": "clb-waf",
                "Region": "gz",
                "Cname": "",
                "ClsStatus": 1,
                "FlowMode": 1,
                "Status": 1,
                "Mode": 1,
                "Engine": 20,
                "RsList": [],
                "CCList": [],
                "Ports": [
                    {
                        "NginxServerId": 0,
                        "Port": "",
                        "Protocol": "",
                        "UpstreamPort": "",
                        "UpstreamProtocol": ""
                    }
                ],
                "LoadBalancerSet": [
                    {
                        "ListenerId": "",
                        "ListenerName": "",
                        "LoadBalancerId": "",
                        "LoadBalancerName": "",
                        "Protocol": "",
                        "Region": "",
                        "Vip": "",
                        "Vport": 0,
                        "Zone": ""
                    }
                ]
            }
        ]
    }
}
```

