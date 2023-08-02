**Example 1: 为客户端节点删除跨vpc子网访问能力**

为客户端节点删除跨vpc子网访问能力

Input: 

```
tccli goosefs DeleteCrossVpcSubnetSupportForClientNode --cli-unfold-argument  \
    --FileSystemId x-c60-a1b2c3d4 \
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

