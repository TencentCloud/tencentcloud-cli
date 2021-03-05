**Example 1: 获取流量镜像的监听器列表信息**



Input: 

```
tccli bmlb DescribeTrafficMirrorListeners --cli-unfold-argument  \
    --TrafficMirrorId bmtm-lmep0eit
```

Output: 
```
{
    "Response": {
        "ListenerSet": [
            {
                "ListenerId": "lbl-3b8kycav",
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
                "LoadBalancerName": "5c1-LB"
            }
        ],
        "TotalCount": 1,
        "RequestId": "ac1bf674-f4d9-421e-ac50-de1f46c40238"
    }
}
```

