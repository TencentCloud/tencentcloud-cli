**Example 1: 配置CHC物理服务器的带外和部署网络**

配置CHC物理服务器的带外和部署网络

Input: 

```
tccli cvm ConfigureChcAssistVpc --cli-unfold-argument  \
    --ChcIds chc-1a2b3c4d chc-adf34aft \
    --BmcVirtualPrivateCloud.SubnetId "subnet-12345678" \
    --BmcVirtualPrivateCloud.VpcId "vpc-12345678" \
    --BmcVirtualPrivateCloud.PrivateIpAddresses 10.0.0.2 10.0.0.3 \
    --BmcSecurityGroupIds sg-12345678 \
    --DeployVirtualPrivateCloud.SubnetId "subnet-1234abcd" \
    --DeployVirtualPrivateCloud.VpcId "vpc-1234abcd8" \
    --DeployVirtualPrivateCloud.PrivateIpAddresses 10.0.1.2 10.0.1.3 \
    --DeploySecurityGroupIds sg-8a7f6d5s
```

Output: 
```
{
    "Response": {
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

