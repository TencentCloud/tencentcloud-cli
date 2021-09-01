**Example 1: NAT网关绑定IP**



Input: 

```
tccli bmvpc BindIpsToNatGateway --cli-unfold-argument  \
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
        "TaskId": 18425,
        "RequestId": "758c3c3b-1f86-4930-a533-99549fc14a2c"
    }
}
```

