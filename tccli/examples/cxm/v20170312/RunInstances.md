**Example 1: 创建eks**

创建eks

Input: 

```
tccli cxm RunInstances --cli-unfold-argument  \
    --DryRun False \
    --InstanceCount 1 \
    --InstanceIds eks-a3fvbrt7 \
    --ImageId img-eb30mz89 \
    --HostName diluczhang \
    --InstanceType S5.MEDIUM2 \
    --PurchaseSource eks \
    --SecurityGroupIds sg-rjgrzrf6 \
    --UserData IyEvYmluL2Jhc2gKRE... \
    --ProductCategory eks \
    --CamRoleName TKE_QCSLinkedRoleInEKSLog \
    --SoldPool plain \
    --ReservedPackMatchId cls-ouh23thx_eklet-subnet-3x3weezp-743923 \
    --SystemDisk.DiskId disk-0qxpl3ni \
    --VirtualPrivateCloud.VpcId vpc-7j6i9bb9 \
    --VirtualPrivateCloud.SubnetId subnet-5gnb3uz4 \
    --VirtualPrivateCloud.AsVpcGateway False \
    --VirtualPrivateCloud.SpecifyIpAddresses 30.0.0.26 \
    --Placement.Zone ap-jinan-ec-1 \
    --Placement.ProjectId 0
```

Output: 
```
{
    "Response": {
        "InstanceIds": [
            "eks-a3fvbrt7"
        ],
        "TaskId": 103241254,
        "RequestId": "ebcc1954-c25d-4338-a592-9811988593e8"
    }
}
```

