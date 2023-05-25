**Example 1: 升级Cynos内核版本**



Input: 

```
tccli cynosdb UpgradeClusterVersion --cli-unfold-argument  \
    --ClusterId xxx \
    --CynosVersion 2.0.0 \
    --UpgradeType upgradeImmediate
```

Output: 
```
{
    "Response": {
        "RequestId": "128046",
        "FlowId": "123"
    }
}
```

