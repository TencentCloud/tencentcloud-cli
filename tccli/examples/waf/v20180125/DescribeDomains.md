**Example 1: 查询用户所有域名信息**

查询用户所有域名信息

Input: 

```
tccli waf DescribeDomains --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "RequestId": "93efef98-b938-4ae7-bad3-19fc70b7b9a7",
        "Total": 2,
        "Domains": [
            {
                "AppId": 1256704386,
                "Domain": "zhenhas1020.qcloudwaf.com",
                "DomainId": "waf-ApUwCv4q",
                "InstanceId": "waf_2k0il2fm02vqm7z3",
                "InstanceName": "cd-Default1",
                "Edition": "clb-waf",
                "Region": "cd",
                "CreateTime": "2024-10-28T16:52:33+08:00",
                "Cname": "dae1cae7d48ec31c7727a86a5c1a2a62.qcloudzygj.com",
                "ClsStatus": 0,
                "PostCLSStatus": 0,
                "PostCKafkaStatus": 0,
                "FlowMode": 1,
                "Status": 1,
                "Mode": 1,
                "State": 0,
                "Engine": 20,
                "Ipv6Status": 0,
                "BotStatus": 2,
                "ApiStatus": 0,
                "Level": 3,
                "CdcClusters": "cls-dasjh2a2t5",
                "RsList": [
                    "1.14.1.0/24"
                ],
                "CCList": [
                    "1.14.3.0/24"
                ],
                "Ports": [
                    {
                        "NginxServerId": 257856,
                        "Port": "80",
                        "Protocol": "http",
                        "UpstreamPort": "80",
                        "UpstreamProtocol": "http"
                    }
                ],
                "LoadBalancerSet": [
                    {
                        "ListenerId": "lbl-d823da3",
                        "ListenerName": "listener 80",
                        "LoadBalancerId": "lb-nda52sau",
                        "LoadBalancerName": "cd lb",
                        "Protocol": "HTTP",
                        "Region": "cd",
                        "Vip": "26.153.3.235",
                        "Vport": 80,
                        "Zone": "ap-chengdu-1",
                        "NumericalVpcId": 23654,
                        "LoadBalancerType": "OPEN",
                        "LoadBalancerDomain": "lb-nda52sau-vo1x4syum7jtqz5n.clb.ap-guangzhou.tencentclb.com"
                    }
                ],
                "AlbType": "clb",
                "SgState": 0,
                "CloudType": "public",
                "Note": "clb domain",
                "AccessStatus": 1,
                "Labels": [
                    "clb domain"
                ]
            },
            {
                "AppId": 1256704386,
                "Domain": "zhenhuasaas1020.qcloudwaf.com",
                "DomainId": "11c88f0f292a5fd4a3002344271367b2",
                "InstanceId": "waf_2kzh5tma0v0jpotj",
                "InstanceName": "cd-Default",
                "Edition": "sparta-waf",
                "Region": "cd",
                "CreateTime": "2024-10-21T14:41:50+08:00",
                "Cname": "88fa6f44eee830c8e1e3b3c5ecba6af7.qcloudzygj.com",
                "ClsStatus": 1,
                "PostCLSStatus": 0,
                "PostCKafkaStatus": 0,
                "FlowMode": 0,
                "Status": 1,
                "Mode": 1,
                "State": 0,
                "Engine": 1,
                "Ipv6Status": 0,
                "BotStatus": 0,
                "ApiStatus": 0,
                "Level": 3,
                "RsList": [
                    "1.14.1.0/24"
                ],
                "CCList": [
                    "1.14.8.0/24"
                ],
                "Ports": [
                    {
                        "NginxServerId": 329025,
                        "Port": "80",
                        "Protocol": "http",
                        "UpstreamPort": "80",
                        "UpstreamProtocol": "http"
                    }
                ],
                "LoadBalancerSet": [
                    {
                        "ListenerId": "default",
                        "ListenerName": "default",
                        "LoadBalancerId": "default.cd",
                        "LoadBalancerName": "default.clb",
                        "Protocol": "HTTP",
                        "Region": "cd",
                        "Vip": "8.8.8.8",
                        "Vport": 80,
                        "Zone": "cd",
                        "NumericalVpcId": -1,
                        "LoadBalancerType": "OPEN",
                        "LoadBalancerDomain": "default.cd"
                    }
                ],
                "SgState": 1,
                "SgDetail": "ok",
                "CloudType": "public",
                "Note": "saas domain",
                "SrcList": [
                    "87.29.132.9"
                ],
                "SgID": "sg-asn32ag1",
                "AccessStatus": 1,
                "Labels": [
                    "saas domain"
                ]
            }
        ]
    }
}
```

**Example 2: 查询用户SAASWAF某个实例的域名信息**

查询用户SAASWAF某个实例的域名信息

Input: 

```
tccli waf DescribeDomains --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name Edition \
    --Filters.0.Values sparta_waf \
    --Filters.0.ExactMatch True \
    --Filters.1.Name InstanceId \
    --Filters.1.Values waf_2kw60jgy0908e8j3 \
    --Filters.1.ExactMatch True
```

Output: 
```
{
    "Response": {
        "RequestId": "91334a5a-1d24-42b9-998e-57e1490f9608",
        "Total": 2,
        "Domains": [
            {
                "AppId": 1256702383,
                "Domain": "randygz2.qcloudwaf.com",
                "DomainId": "7d58ebf3db7e5f7e8f91eb017c6a7b31",
                "InstanceId": "waf_2kw60jgy0908e8j3",
                "InstanceName": "广州双栈集群企业版",
                "Edition": "sparta-waf",
                "Region": "gz",
                "CreateTime": "2024-07-18T10:46:12+08:00",
                "Cname": "dae1cae7d48ec31c7727a86a8cda2a62.qcloudzygj.com",
                "ClsStatus": 1,
                "PostCLSStatus": 0,
                "PostCKafkaStatus": 0,
                "FlowMode": 0,
                "Status": 1,
                "Mode": 1,
                "State": 0,
                "Engine": 1,
                "Ipv6Status": 1,
                "BotStatus": 2,
                "ApiStatus": 0,
                "Level": 3,
                "RsList": [
                    "134.175.221.0/24",
                    "2402:4e00:1020:1707::/64"
                ],
                "CCList": [
                    "134.175.225.0/24"
                ],
                "Ports": [
                    {
                        "NginxServerId": 231056,
                        "Port": "80",
                        "Protocol": "http",
                        "UpstreamPort": "80",
                        "UpstreamProtocol": "http"
                    },
                    {
                        "NginxServerId": 321607,
                        "Port": "443",
                        "Protocol": "https",
                        "UpstreamPort": "80",
                        "UpstreamProtocol": "http"
                    }
                ],
                "LoadBalancerSet": [],
                "SgState": 2,
                "SgDetail": "ok",
                "Note": "randy domain",
                "SrcList": [
                    "114.132.246.237"
                ],
                "UpstreamDomainList": [
                    "xiaochegnxu.upstream.com"
                ],
                "SgID": "sg-7dme0v73",
                "AccessStatus": 1,
                "Labels": [
                    "randy domain"
                ]
            },
            {
                "AppId": 1256704386,
                "Domain": "xiaochengxu.qcloudwaf.com",
                "DomainId": "42059f9a9905519d8f9e72a823891544",
                "InstanceId": "waf_2kw60jgy0908e8j3",
                "InstanceName": "广州双栈集群企业版",
                "Edition": "sparta-waf",
                "Region": "gz",
                "CreateTime": "2024-07-08T17:42:42+08:00",
                "Cname": "3323d11c0772e26ca3c68548b9cd069f.qcloudzygj.com",
                "ClsStatus": 1,
                "PostCLSStatus": 0,
                "PostCKafkaStatus": 0,
                "FlowMode": 0,
                "Status": 1,
                "Mode": 1,
                "State": 1,
                "Engine": 1,
                "Ipv6Status": 0,
                "BotStatus": 2,
                "ApiStatus": 0,
                "Level": 3,
                "RsList": [
                    "134.175.221.0/24"
                ],
                "CCList": [
                    "134.175.225.0/24"
                ],
                "Ports": [
                    {
                        "NginxServerId": 257856,
                        "Port": "80",
                        "Protocol": "http",
                        "UpstreamPort": "80",
                        "UpstreamProtocol": "http"
                    }
                ],
                "LoadBalancerSet": [],
                "SgState": 1,
                "SgDetail": "fail",
                "Note": "xiaochengxu",
                "SrcList": [
                    "124.221.148.62"
                ],
                "UpstreamDomainList": [
                    "xiaochegnxu.upstream.com"
                ],
                "SgID": "sg-7dme0v73",
                "AccessStatus": 1,
                "Labels": [
                    "xiaochengxu"
                ]
            }
        ]
    }
}
```

