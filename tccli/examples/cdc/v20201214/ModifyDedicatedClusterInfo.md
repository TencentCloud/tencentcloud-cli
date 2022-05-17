**Example 1: 修改本地专用集群信息**



Input: 

```
tccli cdc ModifyDedicatedClusterInfo --cli-unfold-argument  \
    --DedicatedClusterId cluster-xx \
    --Description xxx \
    --Zone xxx \
    --Name xxx \
    --SiteId xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "3ceeecd2-2f24-4b3f-81eb-3461376xxc2f"
    }
}
```

