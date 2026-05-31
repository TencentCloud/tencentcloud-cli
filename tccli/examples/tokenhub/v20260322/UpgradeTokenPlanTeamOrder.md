**Example 1: 成功调用**



Input: 

```
tccli tokenhub UpgradeTokenPlanTeamOrder --cli-unfold-argument  \
    --TeamId tp-ent-abcdefgh \
    --NewCreditOrToken 1000000
```

Output: 
```
{
    "Response": {
        "BigOrderId": "big-order-id",
        "RequestId": "1ef43aa6-e830-4174-bfcd-d092e7e59bad"
    }
}
```

