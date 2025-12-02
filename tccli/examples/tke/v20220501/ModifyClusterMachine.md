**Example 1: 修改节点自动续费标识**



Input: 

```
tccli tke ModifyClusterMachine --cli-unfold-argument  \
    --ClusterId cls-dg5wylw \
    --MachineNames np-hg57ffaw-jkioi \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW
```

Output: 
```
{
    "Response": {
        "RequestId": "7d6c3318-b802-4416-ba7a-eb527379eb31"
    }
}
```

