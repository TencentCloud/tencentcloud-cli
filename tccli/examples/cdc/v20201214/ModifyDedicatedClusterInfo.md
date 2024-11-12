**Example 1: 修改本地专用集群信息**

修改本地专用集群信息

Input: 

```
tccli cdc ModifyDedicatedClusterInfo --cli-unfold-argument  \
    --DedicatedClusterId cluster-dfaf323 \
    --Description 专用集群 \
    --Zone ap-guangzhou-2 \
    --Name 专用集群 \
    --SiteId site-pp2cbp9k
```

Output: 
```
{
    "Response": {
        "RequestId": "3ceeecd2-2f24-4b3f-81eb-3461376xxc2f"
    }
}
```

