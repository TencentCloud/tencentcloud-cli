**Example 1: 预热用户 VPC 可达第三方镜像**



Input: 

```
tccli ags CreatePreCacheImageTask --cli-unfold-argument  \
    --Image harbor.internal.example.com/team/app:1.0 \
    --ImageRegistryType custom \
    --ImageRegistryConfig.CredentialId agc-xxxxxxxx \
    --ImageRegistryConfig.NetworkConfig.VpcId vpc-xxxxxxxx \
    --ImageRegistryConfig.NetworkConfig.SubnetId subnet-xxxxxxxx \
    --ImageRegistryConfig.NetworkConfig.SecurityGroupId sg-xxxxxxxx \
    --TimeoutMinutes 120
```

Output: 
```
{
    "Response": {
        "Image": "harbor.internal.example.com/team/app:1.0",
        "ImageDigest": "sha256:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "ImageRegistryType": "custom",
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

