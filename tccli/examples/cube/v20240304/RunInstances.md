**Example 1: 创建实例**

创建一个实例

Input: 

```
tccli cube RunInstances --cli-unfold-argument  \
    --InstanceIds ins-2 \
    --VirtualPrivateCloud.SubnetId subnet-dcs9x3gz \
    --VirtualPrivateCloud.VpcId vpc-1urkhbj4 \
    --VirtualPrivateCloud.PrivateIpAddresses 10.0.0.17 \
    --InstanceCount 1 \
    --Placement.Zone ap-shanghai-2 \
    --SystemDisk.DiskSize 50 \
    --SecurityGroupIds sg-arlffnvg \
    --ImageId eks-guestos:0.1 \
    --CPU 50 \
    --Memory 1024 \
    --CpuType INTEL \
    --UserData TXlVc2VyRGF0YQo=
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-1vogaxgk"
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

