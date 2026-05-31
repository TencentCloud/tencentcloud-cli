**Example 1: 成功调用**



Input: 

```
tccli tokenhub CreateTokenPlanTeamOrderAndBuy --cli-unfold-argument  \
    --ProductType enterprise \
    --TeamName test-team \
    --TimeSpan 1 \
    --CreditOrToken 500000 \
    --EnableAutoRenew False
```

Output: 
```
{
    "Response": {
        "BigOrderId": "big-order-id",
        "RequestId": "83c3a50c-370f-42da-bb89-8231fe73d125"
    }
}
```

