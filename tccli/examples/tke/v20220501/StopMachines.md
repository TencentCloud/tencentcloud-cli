**Example 1: 关闭原生节点实例**

关闭原生节点实例

Input: 

```
tccli tke StopMachines --cli-unfold-argument  \
    --ClusterId cls-0dku0jec \
    --MachineNames np-5tx2l4dc-4srqm \
    --StopType soft
```

Output: 
```
{
    "Response": {
        "RequestId": "a27a0c33-fe13-4373-bc88-863791d68f61"
    }
}
```

