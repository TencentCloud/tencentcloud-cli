**Example 1: 示例1**

创建实例

Input: 

```
tccli keewidb CreateInstances --cli-unfold-argument  \
    --ShardNum 3 \
    --TypeId 14 \
    --GoodsNum 1 \
    --UniqVpcId vpc-qicyv9mz \
    --MachineMemory 2 \
    --Period 1 \
    --ZoneId 100002 \
    --ReplicasNum 1 \
    --UniqSubnetId subnet-4rohwntq \
    --DiskSize 100 \
    --MemSize 8 \
    --MachineCpu 1 \
    --Password Test123456 \
    --InstanceName 测试实例2 \
    --BillingMode 1
```

Output: 
```
{
    "Response": {
        "DealId": "229126199",
        "InstanceIds": [
            "kee-emg6bltn"
        ],
        "RequestId": "365b3029-06d5-4016-8054-518994bba781"
    }
}
```

