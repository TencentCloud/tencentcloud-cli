**Example 1: 复制服务器舰队**



Input: 

```
tccli gse CopyFleet --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-2m6pzf4g \
    --AssetId asset-qrdiw1a9 \
    --Description 'Human description' \
    --InstanceType S5.LARGE8 \
    --FleetType ON_DEMAND \
    --Name testfleet \
    --NewGameServerSessionProtectionPolicy TimeLimitProtection \
    --ResourceCreationLimitPolicy.NewGameServerSessionsPerCreator 2 \
    --ResourceCreationLimitPolicy.PolicyPeriodInMinutes 0 \
    --RuntimeConfiguration.GameServerSessionActivationTimeoutSeconds 5 \
    --RuntimeConfiguration.MaxConcurrentGameServerSessionActivations 5 \
    --RuntimeConfiguration.ServerProcesses.0.ConcurrentExecutions 10 \
    --RuntimeConfiguration.ServerProcesses.0.LaunchPath /local/game/GameLiftLinuxServer \
    --InboundPermissions.0.FromPort 1900 \
    --InboundPermissions.0.IpRange 0.0.0.0/0 \
    --InboundPermissions.0.Protocol TCP \
    --InboundPermissions.0.ToPort 2900 \
    --SelectedScalingType SCALING_UNSELECTED \
    --SelectedCcnType CCN_UNSELECTED \
    --SelectedTimerType TIMER_UNSELECTED \
    --CopyNumber 1 \
    --DataDiskInfo.0.DiskType CLOUD_PREMIUM \
    --DataDiskInfo.0.DiskSize 50 \
    --SystemDiskInfo.DiskType CLOUD_PREMIUM \
    --SystemDiskInfo.DiskSize 50
```

Output: 
```
{
    "Response": {
        "FleetAttributes": [
            {
                "AssetId": "asset-qrdiw1a9",
                "BillingStatus": "BILLING_ACTIVATED",
                "CreationTime": "2020-11-18T04:01:03Z",
                "Description": "Human description test update",
                "FleetArn": "qcs::gse:ap-shanghai:uin/838831829:fleet/fleet-qp3g3caa-95z2gimq",
                "FleetId": "fleet-qp3g3caa-95z2gimq",
                "FleetType": "ON_DEMAND",
                "GameServerSessionProtectionTimeLimit": 60,
                "InstanceType": "S5.LARGE8",
                "Name": "frederickli-test-fleet",
                "NewGameServerSessionProtectionPolicy": "TimeLimitProtection",
                "OperatingSystem": "CentOS 7.16 64位",
                "ResourceCreationLimitPolicy": {
                    "NewGameServerSessionsPerCreator": 2,
                    "PolicyPeriodInMinutes": 3
                },
                "Status": "NEW",
                "StoppedActions": [],
                "TerminationTime": null,
                "DataDiskInfo": [
                    {
                        "DiskType": "CLOUD_PREMIUM",
                        "DiskSize": 50
                    }
                ],
                "SystemDiskInfo": {
                    "DiskType": "CLOUD_PREMIUM",
                    "DiskSize": 50
                }
            }
        ],
        "RequestId": "s1605672063311364390",
        "TotalCount": 1
    }
}
```

