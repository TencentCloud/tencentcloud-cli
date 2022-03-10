**Example 1: 查询匹配的镜像缓存**



Input: 

```
tccli tke GetMostSuitableImageCache --cli-unfold-argument  \
    --Images nginx:latest
```

Output: 
```
{
    "Response": {
        "RequestId": "ccccc-5ed9-4cb7-9194-a95e2cd626e5",
        "Found": false,
        "ImageCache": null
    }
}
```

