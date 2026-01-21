**Example 1: 批量删除客户端节点**

批量添加客户端节点

Input: 

```
tccli goosefs BatchDeleteClientNodes --cli-unfold-argument  \
    --FileSystemId x-c60-80k2ly5b \
    --ClientNodes.0.InstanceId ins-kf9u9pih \
    --ClientNodes.0.VpcId vpc-lc0aecbo \
    --ClientNodes.0.SubnetId subnet-jwtwc1vj \
    --ClientNodes.0.LinuxClientNodeIp 10.3.7.21 \
    --ClusterId x-c60-80k2ly5b-1
```

Output: 
```
{
    "Response": {
        "RequestId": "da09ef86-994b-4358-bc55-6f605f62a070"
    }
}
```

