**Example 1: NAT网关解绑IP**



Input: 

```
tccli bmvpc UnbindIpsFromNatGateway --cli-unfold-argument  \
    --NatId nat-1tw1oc0t \
    --VpcId vpc-mi51u7gs \
    --IpInfoSet.0.SubnetId subnet-qnh7qryt \
    --IpInfoSet.0.Ips 192.168.88.2 \
    --IpInfoSet.1.SubnetId subnet-o9lo3es1 \
    --IpInfoSet.1.Ips 192.168.222.2 192.168.222.3
```

Output: 
```
{
    "Response": {
        "TaskId": 18427,
        "RequestId": "e563a40e-95d9-4d00-8807-3e0fd3efcd0b"
    }
}
```

