**Example 1: 创建镜像加速服务**



Input: 

```
tccli tcr CreateImageAccelerationService --cli-unfold-argument  \
    --RegistryId xxx \
    --VpcId xxx \
    --SubnetId xxx \
    --StorageType xxx \
    --PGroupId xxx \
    --Zone xxx
```

Output: 
```
{
    "Response": {
        "RegistryId": "XXXX",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

