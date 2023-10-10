**Example 1: 批量修改防勒索策略状态**



Input: 

```
tccli cwp ModifyRansomDefenseStrategyStatus --cli-unfold-argument  \
    --Status 1 \
    --IsAll 1 \
    --IdList 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

