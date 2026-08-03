**Example 1: 查询用户 VPC 可达第三方镜像预热状态**



Input: 

```
tccli ags DescribePreCacheImageTask --cli-unfold-argument  \
    --Image harbor.internal.example.com/team/app:1.0 \
    --ImageDigest sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx \
    --ImageRegistryType custom
```

Output: 
```
{
    "Response": {
        "Image": "harbor.internal.example.com/team/app:1.0",
        "ImageDigest": "sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "ImageRegistryType": "custom",
        "Status": "Success",
        "Message": "conversion-backed precache completed",
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

