**Example 1: 更新服务器舰队安全组**

更新服务器舰队安全组

Input: 

```
tccli gse UpdateFleetPortSettings --cli-unfold-argument  \
    --FleetId fleet-pro4eunl-lmpa6tud \
    --InboundPermissionAuthorizations.0.FromPort 1900 \
    --InboundPermissionAuthorizations.0.IpRange 0.0.0.1/0 \
    --InboundPermissionAuthorizations.0.Protocol UDP \
    --InboundPermissionAuthorizations.0.ToPort 2900 \
    --InboundPermissionRevocations.0.FromPort 19000 \
    --InboundPermissionRevocations.0.IpRange 0.0.0.0/0 \
    --InboundPermissionRevocations.0.Protocol TCP \
    --InboundPermissionRevocations.0.ToPort 24000
```

Output: 
```
{
    "Response": {
        "FleetId": "fleet-pro4eunl-lmpa6tud",
        "RequestId": "2f564325-03c0-4fdb-a099-25376c20723f"
    }
}
```

