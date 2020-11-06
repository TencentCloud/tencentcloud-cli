**Example 1: 更新服务器舰队属性**

更新服务器舰队属性

Input: 

```
tccli gse UpdateFleetAttributes --cli-unfold-argument  \
    --FleetId fleet-pro4eunl-lmpa6tud \
    --Description Modifyfleetattr1 \
    --Name mod1 \
    --NewGameSessionProtectionPolicy FullProtection \
    --ResourceCreationLimitPolicy.NewGameServerSessionsPerCreator 9 \
    --ResourceCreationLimitPolicy.PolicyPeriodInMinutes 9
```

Output: 
```
{
    "Response": {
        "FleetId": "fleet-pro4eunl-lmpa6tud",
        "RequestId": "accaa150-cd32-4919-8283-da31817e6363"
    }
}
```

