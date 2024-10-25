**Example 1: 导入源集群消费组**



Input: 

```
tccli trocket ImportSourceClusterConsumerGroups --cli-unfold-argument  \
    --TaskId n4zk7nv4-d596886f \
    --GroupList.0.GroupName test_group \
    --GroupList.0.Remark 测试 \
    --GroupList.0.Namespace test_namespace
```

Output: 
```
{
    "Response": {
        "RequestId": "c5d126b6-aeeb-40ad-81c0-a94abd43f157"
    }
}
```

