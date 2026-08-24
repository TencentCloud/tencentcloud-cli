**Example 1: 创建保护组**



Input: 

```
tccli bdrc CreateDisasterRecoveryProtectGroup --cli-unfold-argument  \
    --SitePairId sitepair-0wxbktxr \
    --ProtectGroupType INSTANCE \
    --RecoveryPointObjective 15 \
    --ProtectGroupName todelete from api
```

Output: 
```
{
    "Response": {
        "ProtectGroupId": "pg-bb93pcar",
        "RequestId": "f2e157c2-6425-47bd-84bb-c63d6fec1d4e"
    }
}
```

