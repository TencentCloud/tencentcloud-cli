**Example 1: 更新配额自动共享管理团队配置**



Input: 

```
tccli csip ModifyCspmShardConfig --cli-unfold-argument  \
    --AutoShardStatus 2
```

Output: 
```
{
    "Response": {
        "AutoShardStatus": 2,
        "ShardAppIDs": [
            260099082
        ],
        "ShardFromAppID": 260190972,
        "RequestId": "b9a5f648-99bf-43c8-8512-efcdab2e7177"
    }
}
```

