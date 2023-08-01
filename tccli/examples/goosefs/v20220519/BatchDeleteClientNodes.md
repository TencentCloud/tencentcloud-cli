**Example 1: 批量删除客户端节点**

批量添加客户端节点

Input: 

```
tccli goosefs BatchDeleteClientNodes --cli-unfold-argument  \
    --FileSystemId x_c60_r3c4fa1f \
    --SingleClusterFlag False \
    --ClientNodes.0.InstanceId ins-m1r9uwdp \
    --ClientNodes.0.VpcId vpc-5ke3uoww \
    --ClientNodes.0.SubnetId subnet-ihijdp5h \
    --ClientNodes.0.LinuxClientNodeIp 10.0.1.2
```

Output: 
```
{
    "Response": {
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6"
    }
}
```

