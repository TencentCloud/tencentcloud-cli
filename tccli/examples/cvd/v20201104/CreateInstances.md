**Example 1: 创建实例**



Input: 

```
tccli cvd CreateInstances --cli-unfold-argument  \
    --InstanceType S1L.LARGE8 \
    --SystemDisk.DiskType CLOUD_SSD \
    --SystemDisk.DiskSize 50 \
    --ImageId img-40kyb7sr \
    --VirtualPrivateCloud.VpcId vpc-1f99gocg \
    --VirtualPrivateCloud.SubnetId subnet-a2f56ctb \
    --ChargeType POSTPAID_BY_HOUR
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "cdi-th8c2dtr6c4tjqy"
        ],
        "RequestId": "11212ab3-2a95-4f46-9644-019bb237e6e2"
    }
}
```

