**Example 1: 按镜像三元组卸载镜像预热**



Input: 

```
tccli ags DeletePreCacheImage --cli-unfold-argument  \
    --Image ccr.ccs.tencentyun.com/ags.example/nginx:v1 \
    --ImageDigest sha256:d9c56e383f4711392************************41feebfecf42a8755f916bb \
    --ImageRegistryType personal
```

Output: 
```
{
    "Response": {
        "RequestId": "aedbad4c-ede8-46f9-bb02-c693c6a2d6dc"
    }
}
```

**Example 2: 按预热镜像ID卸载镜像预热**



Input: 

```
tccli ags DeletePreCacheImage --cli-unfold-argument  \
    --PreCacheImageId pcimg-7k******
```

Output: 
```
{
    "Response": {
        "RequestId": "fd94bec3-6f82-4338-b650-bde4fda32dfd"
    }
}
```

