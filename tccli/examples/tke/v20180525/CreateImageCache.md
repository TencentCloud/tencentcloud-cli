**Example 1: 创建镜像缓存**



Input: 

```
tccli tke CreateImageCache --cli-unfold-argument  \
    --VpcId vpc-508ctkfb \
    --SubnetId subnet-8ah75lo8 \
    --Images nginx:latest \
    --ImageCacheSize 50
```

Output: 
```
{
    "Response": {
        "RequestId": "232323-5ed9-4cb7-9194-a95e2cd626e5",
        "ImageCacheId": "imc-xxx"
    }
}
```

