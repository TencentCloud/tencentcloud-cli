**Example 1: 批量添加客户端节点**

批量添加客户端节点

Input: 

```
tccli goosefs BatchAddClientNodes --cli-unfold-argument  \
    --FileSystemId x-c60-80k2ly5b \
    --ClientNodes.0.InstanceId ins-kf9u9pih \
    --ClientNodes.0.VpcId vpc-lc0aecbo \
    --ClientNodes.0.SubnetId subnet-jwtwc1vj \
    --ClientNodes.0.LinuxClientNodeIp 10.3.7.21 \
    --ClientNodes.0.MountPoint /Goosefsx \
    --ClusterId x-c60-80k2ly5b-1
```

Output: 
```
{
    "Response": {
        "RequestId": "50bb8fe8-068e-4804-83c6-2f7ed32d88a7"
    }
}
```

