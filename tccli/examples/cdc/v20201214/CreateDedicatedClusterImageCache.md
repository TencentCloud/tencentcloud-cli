**Example 1: 创建云上镜像缓存**

创建云上镜像缓存

Input: 

```
tccli cdc CreateDedicatedClusterImageCache --cli-unfold-argument  \
    --DedicatedClusterId cluster-d8htgb6k \
    --ImageId img-1n0le98u
```

Output: 
```
{
    "Response": {
        "TaskId": 15249,
        "RequestId": "b621f9e4-ea1c-455c-98b4-7f85d857f222"
    }
}
```

