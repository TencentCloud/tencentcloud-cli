**Example 1: 实例proxy升级**



Input: 

```
tccli redis UpgradeProxyVersion --cli-unfold-argument  \
    --InstanceId crs-94w4mqbt \
    --CurrentProxyVersion 4.1.1 \
    --UpgradeProxyVersion 4.3.0 \
    --InstanceTypeUpgradeNow 1
```

Output: 
```
{
    "Response": {
        "FlowId": 327,
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522"
    }
}
```

