**Example 1: 创建服务器舰队**

创建服务器舰队

Input: 

```
tccli gse CreateFleet --cli-unfold-argument  \
    --AssetId asset-eugdyx0g \
    --Description Humandecription \
    --InstanceType S5.LARGE8 \
    --FleetType ON_DEMAND \
    --Name testfleet \
    --NewGameServerSessionProtectionPolicy FullProtection \
    --PeerVpcId null \
    --ResourceCreationLimitPolicy.NewGameServerSessionsPerCreator 0 \
    --ResourceCreationLimitPolicy.PolicyPeriodInMinutes 1 \
    --RuntimeConfiguration.GameServerSessionActivationTimeoutSeconds 5 \
    --RuntimeConfiguration.MaxConcurrentGameServerSessionActivations 4 \
    --RuntimeConfiguration.ServerProcesses.0.ConcurrentExecutions 10 \
    --RuntimeConfiguration.ServerProcesses.0.LaunchPath /local/game/GameLiftLinuxServer \
    --RuntimeConfiguration.ServerProcesses.0.Parameters -cconf/config.toml \
    --InboundPermissions.0.FromPort 1900 \
    --InboundPermissions.0.IpRange 0.0.0.0/0 \
    --InboundPermissions.0.Protocol TCP \
    --InboundPermissions.0.ToPort 2900 \
    --DataDiskInfo.0.DiskType CLOUD_PREMIUM \
    --DataDiskInfo.0.DiskSize 50 \
    --SystemDiskInfo.DiskType CLOUD_PREMIUM \
    --SystemDiskInfo.DiskSize 50
```

Output: 
```
{
    "Response": {
        "FleetAttributes": {
            "AssetId": "build-xifjw-fiist-2019",
            "CreationTime": "2019-12-09T13:37:01Z",
            "Description": "Human decription",
            "FleetArn": "qcs::gse:ap-beijing:uin/20548499:fleet/fleet-pro4eunl-0l1exqxf",
            "FleetId": "fleet-pro4eunl-0l1exqxf",
            "FleetType": "ON_DEMAND",
            "GameServerSessionProtectionTimeLimit": 5,
            "InstanceType": "S5.LARGE8",
            "Name": "test fleet",
            "NewGameServerSessionProtectionPolicy": "TimeLimitProtection",
            "OperatingSystem": "centos",
            "ResourceCreationLimitPolicy": {
                "NewGameServerSessionsPerCreator": 0,
                "PolicyPeriodInMinutes": 1
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
        },
        "RequestId": "4520ba54-982e-46e2-9a0b-63c963c34fc6"
    }
}
```

