**Example 1: 网段方式创建NAT网关**



Input: 

```
tccli bmvpc CreateNatGateway --cli-unfold-argument  \
    --ForwardMode 1 \
    --VpcId vpc-mi51u7gs \
    --NatName test \
    --MaxConcurrent 10000000 \
    --AssignedEips 139.199.40.59 \
    --SubnetIds subnet-d3668cur subnet-dipbsl5n
```

Output: 
```
{
    "Response": {
        "TaskId": 18403,
        "RequestId": "6e9f212d-b3cb-417e-b78e-3ae6ec690e4d"
    }
}
```

**Example 2: IP方式创建NAT网关**



Input: 

```
tccli bmvpc CreateNatGateway --cli-unfold-argument  \
    --ForwardMode 0 \
    --VpcId vpc-mi51u7gs \
    --SubnetIds subnet-kmoq5ugh subnet-j74dmsz5 \
    --IpInfoSet.0.SubnetId subnet-qnh7qryt \
    --IpInfoSet.0.Ips 192.168.88.2 \
    --IpInfoSet.1.SubnetId subnet-o9lo3es1 \
    --IpInfoSet.1.Ips 192.168.222.2 192.168.222.3 \
    --NatName test \
    --MaxConcurrent 1000000 \
    --AutoAllocEipNum 1
```

Output: 
```
{
    "Response": {
        "TaskId": 18405,
        "RequestId": "7d18fca8-4b3c-4bc6-818e-ec291764b8fb"
    }
}
```

