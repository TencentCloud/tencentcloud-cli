**Example 1: 根据VPC获取所有的7层监听器**



Input: 

```
tccli bmlb DescribeL7ListenersEx --cli-unfold-argument  \
    --TrafficMirrorId bmtm-lmep0eit \
    --VpcId vpc-muinpf9p
```

Output: 
```
{
    "Response": {
        "ListenerSet": [
            {
                "ListenerId": "",
                "ListenerName": "http",
                "Protocol": "http",
                "LoadBalancerPort": 80,
                "Bandwidth": 0,
                "MaxBandwidth": 0,
                "ListenerType": "L7Listener",
                "CertId": "",
                "CertCaId": "",
                "AddTimestamp": "2018-10-11 15:29:42",
                "LoadBalancerId": "lb-gdr96fc7",
                "VpcName": "cassiehe",
                "VpcCidrBlock": "10.1.0.0/16",
                "LoadBalancerVips": [
                    "115.159.240.85"
                ],
                "LoadBalancerVipv6s": [
                    ""
                ],
                "BindTrafficMirror": true,
                "LoadBalancerName": "5c1-LB"
            },
            {
                "ListenerId": "",
                "ListenerName": "https",
                "Protocol": "https",
                "LoadBalancerPort": 443,
                "Bandwidth": 0,
                "MaxBandwidth": 0,
                "ListenerType": "L7Listener",
                "CertId": "LnSy875s",
                "CertCaId": "",
                "AddTimestamp": "2018-10-11 15:56:43",
                "LoadBalancerId": "lb-gdr96fc7",
                "VpcName": "cassiehe",
                "VpcCidrBlock": "10.1.0.0/16",
                "LoadBalancerVips": [
                    "115.159.240.85"
                ],
                "LoadBalancerVipv6s": [
                    ""
                ],
                "BindTrafficMirror": true,
                "LoadBalancerName": "5c1-LB"
            }
        ],
        "TotalCount": 2,
        "RequestId": "0a1a3007-2539-4109-81f8-2a5781439d18"
    }
}
```

