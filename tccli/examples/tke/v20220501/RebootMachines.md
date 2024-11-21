**Example 1: 重启原生节点实例**

该接口支持原生节点重启，重启时限制一次重启的原生节点数量最多为100个

Input: 

```
tccli tke RebootMachines --cli-unfold-argument  \
    --ClusterId cls-0dku0jec \
    --MachineNames np-5tx2l4dc-4srqm np-5tx2l4dc-4srqn \
    --StopType soft
```

Output: 
```
{
    "Response": {
        "RequestId": "3c0b712f-28a8-42a7-a89a-b4448a01421f"
    }
}
```

