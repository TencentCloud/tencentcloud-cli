**Example 1: 续费包年包月Oceanus集群**

续费包年包月Oceanus集群一个月

Input: 

```
tccli oceanus RenewOceanusCluster --cli-unfold-argument  \
    --ClusterId cluster-******** \
    --Period 1
```

Output: 
```
{
    "Response": {
        "TaskExecResult": "success",
        "RequestId": "1dc397ba-37fb-4360-9309-8e8d18b4fa9b"
    }
}
```

