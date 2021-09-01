**Example 1: 用于查询服务器舰队属性**

用于查询服务器舰队属性

Input: 

```
tccli gse DescribeFleetAttributes --cli-unfold-argument  \
    --FleetIds fleet-qp3g3caa-nkeekxw6
```

Output: 
```
{
    "Response": {
        "FleetAttributes": [
            {
                "AssetId": "asset-97n7z87d",
                "BillingStatus": "UNKNOWN",
                "CreationTime": "2020-01-06T09:55:34Z",
                "Description": "范德萨范德萨发",
                "FleetArn": "qcs::gse:ap-shanghai:uin/:fleet/fleet-qp3g3caa-hxcv60fw",
                "FleetId": "fleet-qp3g3caa-hxcv60fw",
                "FleetType": "ON_DEMAND",
                "GameServerSessionProtectionTimeLimit": 0,
                "InstanceType": "S5.SMALL2",
                "Name": "tedt01",
                "NewGameServerSessionProtectionPolicy": "FullProtection",
                "OperatingSystem": "",
                "ResourceCreationLimitPolicy": {
                    "NewGameServerSessionsPerCreator": 2,
                    "PolicyPeriodInMinutes": 3
                },
                "Status": "ACTIVE",
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
        "RequestId": "s1602557884795276136",
        "TotalCount": 1
    }
}
```

