**Example 1: 删除原生节点池节点**



Input: 

```
tccli tke DeleteClusterMachines --cli-unfold-argument  \
    --MachineNames np-5tx2l4dc-hbbv6 \
    --ClusterId cls-l9l1o3y0 \
    --EnableScaleDown False
```

Output: 
```
{
    "Response": {
        "RequestId": "71e54a99-9be0-4983-82ff-54dce2191c4a"
    }
}
```

