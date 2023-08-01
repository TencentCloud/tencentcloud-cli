**Example 1: 为客户端节点添加跨vpc和子网访问的能力**

为客户端节点添加跨vpc和子网访问的能力

Input: 

```
tccli goosefs AddCrossVpcSubnetSupportForClientNode --cli-unfold-argument  \
    --FileSystemId x-c60-r3c4fa1f \
    --SubnetInfo.VpcId vpc-a1b2c3d4 \
    --SubnetInfo.SubnetId subnet-a1b2c3d4
```

Output: 
```
{
    "Response": {
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6"
    }
}
```

