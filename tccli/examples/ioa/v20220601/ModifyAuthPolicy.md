**Example 1: ModifyAuthPolicy**



Input: 

```
tccli ioa ModifyAuthPolicy --cli-unfold-argument  \
    --PolicyName 自定义认证策略-修改 \
    --ScopeItems.0.List.0.Name 认证联调 \
    --ScopeItems.0.List.0.Id 113 \
    --ScopeItems.0.ScopeType 2 \
    --PolicyPriority 1 \
    --Description 认证策略描述 \
    --PcAuthConfig.0.AuthSwitch 2 \
    --PcAuthConfig.0.AuthState 1 \
    --PcAuthConfig.0.ExtraConfig.AvoidSecondAuthSwitch 1 \
    --PcAuthConfig.0.ExtraConfig.AvoidAuthSource.0.AuthSourceGuid  \
    --PcAuthConfig.0.ExtraConfig.AvoidAuthSource.0.AuthSourceId 1 \
    --PcAuthConfig.0.ExtraConfig.AvoidAuthSource.0.AuthSourceName  \
    --PcAuthConfig.0.AdAutoLoginSwitch 2 \
    --PcAuthConfig.0.AuthSourceArray.0.AuthSourceGuid iOA \
    --PcAuthConfig.0.AuthSourceArray.0.AuthSourceId 5 \
    --PcAuthConfig.0.AuthSourceArray.0.AuthSourceName iOA本地账密 \
    --PolicyType 2 \
    --PolicyId 15 \
    --MobileAuthConfig.0.AuthSwitch 2 \
    --MobileAuthConfig.0.AuthState 1 \
    --MobileAuthConfig.0.ExtraConfig.AvoidSecondAuthSwitch 1 \
    --MobileAuthConfig.0.ExtraConfig.AvoidAuthSource.0.AuthSourceGuid  \
    --MobileAuthConfig.0.ExtraConfig.AvoidAuthSource.0.AuthSourceId 1 \
    --MobileAuthConfig.0.ExtraConfig.AvoidAuthSource.0.AuthSourceName  \
    --MobileAuthConfig.0.AdAutoLoginSwitch 2 \
    --MobileAuthConfig.0.AuthSourceArray.0.AuthSourceGuid iOA \
    --MobileAuthConfig.0.AuthSourceArray.0.AuthSourceId 5 \
    --MobileAuthConfig.0.AuthSourceArray.0.AuthSourceName iOA本地账密 \
    --GroupId 113
```

Output: 
```
{
    "Response": {
        "RequestId": "95649fa3-17ff-40b4-a294-5fd347a448da"
    }
}
```

