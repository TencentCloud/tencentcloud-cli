**Example 1: 导入源集群消费组**



Input: 

```
tccli trocket ImportSourceClusterConsumerGroups --cli-unfold-argument  \
    --TaskId abc \
    --GroupList.0.GroupName Test \
    --GroupList.0.Remark abc \
    --GroupList.0.Namespace 
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

