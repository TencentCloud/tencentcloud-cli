**Example 1: 删除本地专用集群的云上镜像缓存**

删除本地专用集群的云上镜像缓存

Input: 

```
tccli cdc DeleteDedicatedClusterImageCache --cli-unfold-argument  \
    --DedicatedClusterId cluster-d8htgb6k \
    --ImageId img-1n0le98u
```

Output: 
```
{
    "Response": {
        "RequestId": "27d4ca38-284b-4ffb-ae1d-e9ff12c065b8"
    }
}
```

