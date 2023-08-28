**Example 1: 主备可用区切换**



Input: 

```
tccli cynosdb SwitchClusterZone --cli-unfold-argument  \
    --ClusterId cynosdbmysql-asd \
    --OldZone ap-guangzhou-2 \
    --NewZone ap-guangzhou-3 \
    --IsInMaintainPeriod yes
```

Output: 
```
{
    "Response": {
        "FlowId": 123,
        "RequestId": "128046"
    }
}
```

