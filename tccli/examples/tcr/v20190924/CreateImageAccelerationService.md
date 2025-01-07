**Example 1: 创建镜像加速服务**



Input: 

```
tccli tcr CreateImageAccelerationService --cli-unfold-argument  \
    --RegistryId tcr-xxx \
    --VpcId vpc-xxx \
    --SubnetId subnet-xxx \
    --StorageType HD \
    --PGroupId groupID \
    --Zone ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RegistryId": "tcr-xxx",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

