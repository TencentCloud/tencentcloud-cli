**Example 1: 创建专用集群**

创建专用集群

Input: 

```
tccli cdc CreateDedicatedCluster --cli-unfold-argument  \
    --SiteId site-98dj3kd \
    --Name my-site \
    --Zone ap-guangzhou \
    --Description site
```

Output: 
```
{
    "Response": {
        "DedicatedClusterId": "cluster-gbo27yc4",
        "RequestId": "d39d6c09-44e9-4e80-8661-77b5ff3cbc15"
    }
}
```

