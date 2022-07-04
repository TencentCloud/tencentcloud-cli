**Example 1: 配置CHC物理服务器的部署网络**

配置CHC物理服务器的部署网络

Input: 

```
tccli cvm ConfigureChcDeployVpc --cli-unfold-argument  \
    --ChcIds chc-1a2b3c4d chc-adf34aft \
    --DeployVirtualPrivateCloud.SubnetId "subnet-1234abcd" \
    --DeployVirtualPrivateCloud.VpcId "vpc-1234abcd8" \
    --DeployVirtualPrivateCloud.PrivateIpAddresses 10.0.1.2 10.0.1.3 \
    --DeploySecurityGroupIds sg-8a7f6d5s \
    --ChcDeployExtraConfig.MiniOsType public \
    --ChcDeployExtraConfig.BootType x86_legacy \
    --ChcDeployExtraConfig.BootFile pxelinux.0 \
    --ChcDeployExtraConfig.NextServerAddress 169.254.68.10
```

Output: 
```
{
    "Response": {
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

