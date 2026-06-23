**Example 1: 创建磁盘加密实例**



Input: 

```
tccli vdb CreateInstance --cli-unfold-argument  \
    --VpcId vpc-n4c3s8u4 \
    --SubnetId subnet-8apk7iir \
    --PayMode 0 \
    --InstanceName vdb-disk \
    --SecurityGroupIds sg-dxnd192j \
    --PayPeriod 1 \
    --AutoRenew 1 \
    --Params None \
    --ResourceTags.0.TagKey None \
    --ResourceTags.0.TagValue None \
    --ProductType 0 \
    --InstanceType cluster \
    --Mode two \
    --GoodsNum 1 \
    --Cpu 1 \
    --Memory 2 \
    --DiskSize 100 \
    --WorkerNodeNum 2 \
    --EnableEncryption False
```

Output: 
```
{
    "Response": {
        "InstanceIds": [
            "vdb-17jsleiv"
        ],
        "RequestId": "617ca492-e31a-445f-b562-8a6588ed2a6b"
    }
}
```

