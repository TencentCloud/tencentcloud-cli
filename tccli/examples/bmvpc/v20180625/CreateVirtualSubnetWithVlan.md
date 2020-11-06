**Example 1: 创建黑石虚拟子网**

创建黑石虚拟子网，虚拟子网专门用于在黑石上做虚拟话。会分配VlanId给虚拟子网。

Input: 

```
tccli bmvpc CreateVirtualSubnetWithVlan --cli-unfold-argument  \
    --VpcId vpc-44cxlz7z \
    --SubnetSet.0.SubnetName ownSubnet1 \
    --SubnetSet.0.CidrBlock 10.10.246.0/26 \
    --SubnetSet.1.SubnetName ownDocker2 \
    --SubnetSet.1.CidrBlock 10.10.246.64/26
```

Output: 
```
{
    "Response": {
        "TaskId": 1234,
        "RequestId": "09186e64-d19e-4ca1-968f-df4fc8139192"
    }
}
```

