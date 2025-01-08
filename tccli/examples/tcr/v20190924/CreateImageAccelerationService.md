**Example 1: 创建镜像加速服务**



Input: 

```
tccli tcr CreateImageAccelerationService --cli-unfold-argument  \
    --RegistryId tcr-safsdfs \
    --VpcId vpc-sadfaf \
    --SubnetId subnet-asfsdfsd \
    --StorageType HD \
    --PGroupId groupID \
    --Zone ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RegistryId": "tcr-safsdfs",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

