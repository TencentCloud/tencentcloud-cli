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
        "RequestId": "347698da-03e4-4078-8d96-9a8b219c01a5",
        "FlowId": "1472831"
    }
}
```

