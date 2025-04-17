**Example 1: cdc镜像同步**

cdc镜像同步

Input: 

```
tccli cdc SyncDedicatedClusterImage --cli-unfold-argument  \
    --DedicatedClusterId cluster-d8htgb6k \
    --ImageId img-1n0le98u \
    --DestinationUin 700000287016 \
    --DestinationDedicatedClusterId cluster-d8htgb6k
```

Output: 
```
{
    "Response": {
        "TaskId": 2801,
        "RequestId": "27d4ca38-284b-4ffb-ae1d-e9ff12c065b8"
    }
}
```

**Example 2: cdc镜像上传到云上**

cdc镜像上传到云上

Input: 

```
tccli cdc SyncDedicatedClusterImage --cli-unfold-argument  \
    --DedicatedClusterId cluster-d8htgb6k \
    --ImageId img-1n0le98u \
    --ImageName test \
    --ImageDescription test \
    --TagSpecification.0.ResourceType image \
    --TagSpecification.0.Tags.0.Key annexwu1 \
    --TagSpecification.0.Tags.0.Value annexwu1-value
```

Output: 
```
{
    "Response": {
        "TaskId": 2801,
        "RequestId": "27d4ca38-284b-4ffb-ae1d-e9ff12c065b8"
    }
}
```

