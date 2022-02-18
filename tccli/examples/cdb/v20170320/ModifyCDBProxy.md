**Example 1: 配置数据库读写分离**



Input: 

```
tccli cdb ModifyCDBProxy --cli-unfold-argument  \
    --MaxDelay 1 \
    --AutoAddRo True \
    --ProxyGroupId proxy-test \
    --IsKickout True \
    --FailOver True \
    --MinCount 1 \
    --WeightMode system
```

Output: 
```
{
    "Response": {
        "RequestId": "122198-2222-1223-2222-c3a1733"
    }
}
```

