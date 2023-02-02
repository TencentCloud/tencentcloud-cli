**Example 1: 给节点池中的节点设置移出保护**

当触发缩容时（包括手动和自动），节点不会被伸缩组从集群中移除

Input: 

```
tccli tke SetNodePoolNodeProtection --cli-unfold-argument  \
    --ProtectedFromScaleIn true \
    --ClusterId cls-xxx \
    --InstanceIds ins-xxx \
    --NodePoolId np-xxx
```

Output: 
```
{
    "Response": {
        "SucceedInstanceIds": [
            "ins-xxx"
        ],
        "FailedInstanceIds": [
            "xx"
        ],
        "RequestId": "xx"
    }
}
```

