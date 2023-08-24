**Example 1: 更新内核小版本**



Input: 

```
tccli cynosdb UpgradeClusterVersion --cli-unfold-argument  \
    --ClusterId cynosdbmysql-qwerasd \
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

