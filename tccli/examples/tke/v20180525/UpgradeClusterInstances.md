**Example 1: 集群节点升级**

给集群的一批work节点进行升级 

Input: 

```
tccli tke UpgradeClusterInstances --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --UpgradeType reset \
    --Operation create \
    --InstanceIds ins-xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

