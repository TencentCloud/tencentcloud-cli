**Example 1: 检查实例端口连通性**



Input: 

```
tccli lighthouse CheckInstanceFirewallPorts --cli-unfold-argument  \
    --InstanceId lhins-q4joas1f \
    --FirewallPorts.0.Protocol TCP \
    --FirewallPorts.0.Port 3389
```

Output: 
```
{
    "Response": {
        "FirewallPortStateSet": [
            {
                "Port": "3389",
                "PortState": "ACCEPT",
                "Protocol": "TCP"
            }
        ],
        "RequestId": "716f32f3-0931-4a47-a9e9-8093257fa924"
    }
}
```

