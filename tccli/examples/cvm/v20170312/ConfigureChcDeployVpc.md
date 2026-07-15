**Example 1: 配置CHC物理服务器的部署网络**

配置CHC物理服务器的部署网络

Input: 

```
tccli cvm ConfigureChcDeployVpc --cli-unfold-argument  \
    --ChcIds chc-ej2pc1yr \
    --DeployVirtualPrivateCloud.VpcId vpc-oa69jq11 \
    --DeployVirtualPrivateCloud.SubnetId subnet-ov1xx3u3 \
    --DeployVirtualPrivateCloud.PrivateIpAddresses 11.97.4.66 \
    --DeploySecurityGroupIds sg-j9ro1lex
```

Output: 
```
{
    "Response": {
        "RequestId": "a35f2e81-435f-4bb0-898c-35e3bc9cb5f3"
    }
}
```

