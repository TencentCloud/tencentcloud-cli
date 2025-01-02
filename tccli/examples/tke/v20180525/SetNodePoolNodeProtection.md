**Example 1: 给节点池中的节点设置移出保护**

当触发缩容时（包括手动和自动），节点不会被伸缩组从集群中移除

Input: 

```
tccli tke SetNodePoolNodeProtection --cli-unfold-argument  \
    --ProtectedFromScaleIn true \
    --ClusterId cls-e55paxnt \
    --InstanceIds ins-e55paxnt \
    --NodePoolId np-e55paxnt
```

Output: 
```
{
    "Response": {
        "SucceedInstanceIds": [
            "ins-rvob5o5"
        ],
        "FailedInstanceIds": [
            "ins-abocc5o"
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

