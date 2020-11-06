**Example 1: 删除集群**

删除集群

Input: 

```
tccli tke DeleteCluster --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx \
    --InstanceDeleteMode terminate
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

