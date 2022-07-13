**Example 1: 迁移实例私有网络且指定子网IP**

实例 r8hr2upy 和 5d8a23rs 迁移至私有网络 1urkhbj4 子网 dcs9x3gz 中，指定实例 r8hr2upy  的私有网络IP为 10.0.0.18，实例 5d8a23rs 的私有网络IP为 10.0.0.19。

Input: 

```
tccli cvm ModifyInstancesVpcAttribute --cli-unfold-argument  \
    --VirtualPrivateCloud.SubnetId subnet-dcs9x3gz \
    --VirtualPrivateCloud.VpcId vpc-1urkhbj4 \
    --VirtualPrivateCloud.PrivateIpAddresses 10.0.0.19 10.0.0.18 \
    --InstanceIds ins-5d8a23rs ins-r8hr2upy
```

Output: 
```
{
    "Response": {
        "RequestId": "3c14def19-cfes-470e-b241-90787u6jf5uj"
    }
}
```

