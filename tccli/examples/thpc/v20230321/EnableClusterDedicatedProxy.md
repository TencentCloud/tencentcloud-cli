**Example 1: 开启IDC集群专线代理**

开启IDC集群的专线/VPN代理，在指定VPC和子网中创建终端节点。

Input: 

```
tccli thpc EnableClusterDedicatedProxy --cli-unfold-argument  \
    --ClusterId hpc-12345678 \
    --VpcId vpc-aaaa1234 \
    --SubnetId subnet-bbbb5678
```

Output: 
```
{
    "Response": {
        "EndPointId": "vpce-12345678",
        "EndPointVip": "10.0.0.1",
        "EndPointReady": true,
        "EndPointStatus": "ACTIVE",
        "VpcId": "vpc-aaaa1234",
        "SubnetId": "subnet-bbbb5678",
        "RequestId": "b2ac2379-6453-4eab-8f63-7ade00cb67b0"
    }
}
```

