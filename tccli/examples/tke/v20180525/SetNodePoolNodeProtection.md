**Example 1: 给节点池中的节点设置移出保护**

当触发缩容时（包括手动和自动），节点不会被伸缩组从集群中移除

Input: 

```
tccli tke SetNodePoolNodeProtection --cli-unfold-argument  \
    --ClusterId cls-xxx \
    --NodePoolId np-xxx \
    --InstanceIds ins-xxx \
    --ProtectedFromScaleIn true
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxx"
    }
}
```

