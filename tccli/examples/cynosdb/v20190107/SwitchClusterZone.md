**Example 1: 主备可用区切换**



Input: 

```
tccli cynosdb SwitchClusterZone --cli-unfold-argument  \
    --ClusterId cynosdbmysql-8f0sh2nj \
    --OldZone ap-guangzhou-3 \
    --NewZone ap-guangzhou-5 \
    --IsInMaintainPeriod no
```

Output: 
```
{
    "Response": {
        "FlowId": 88529647,
        "TaskId": 183430,
        "RequestId": "61e043aa-4b66-4021-a3cb-7b31df93def7"
    }
}
```

