**Example 1: 创建存储板实例**



Input: 

```
tccli keewidb CreateInstances --cli-unfold-argument  \
    --TypeId 12 \
    --UniqVpcId vpc-f76wgk85 \
    --UniqSubnetId subnet-jsmdnv1y \
    --BillingMode 0 \
    --GoodsNum 1 \
    --Period 1 \
    --ShardNum 3 \
    --ReplicasNum 1 \
    --MachineMemory 8 \
    --ZoneId 100006 \
    --InstanceName name1 \
    --Password Test123456 \
    --DiskSize 100 \
    --MachineCpu 2
```

Output: 
```
{
    "Response": {
        "DealId": "20260706185023127858071",
        "DealName": "20260706185023127858071",
        "InstanceIds": [
            "kee-8wb1cgrb"
        ],
        "RequestId": "9af572e5-ab19-4bca-84c6-85109a1350e4"
    }
}
```

