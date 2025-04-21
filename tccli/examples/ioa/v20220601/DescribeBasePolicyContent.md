**Example 1: 查询指定基线策略**



Input: 

```
tccli ioa DescribeBasePolicyContent --cli-unfold-argument  \
    --OsType 0 \
    --PolicyType 1 \
    --PolicySubType 1
```

Output: 
```
{
    "Response": {
        "RequestId": "836b0dbc-1517-45b9-b0f1-21272be7b81d",
        "Data": [
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "TrojanTimedTask",
                "Data": "{\"Enable\":1,\"Tasks\":[{\"Day\":1,\"Hour\":17,\"HourEnd\":18,\"Minute\":0,\"MinuteEnd\":0,\"ScanType\":1,\"TimeType\":1},{\"Day\":1,\"Hour\":0,\"HourEnd\":1,\"Minute\":0,\"MinuteEnd\":0,\"ScanType\":2,\"TimeType\":2}]}",
                "Id": 1
            },
            {
                "Modify": 1,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "TrojanScanSetting",
                "Data": "{\"TrojanScanResource\":1}",
                "Id": 2
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "TrojanCloudType",
                "Data": "{\"TrojanCloudType\":3}",
                "Id": 3
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "AutoReportSuspiciousTrojan",
                "Data": "{\"Switch\":1}",
                "Id": 4
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "NetpathScanEnable",
                "Data": "{\"Switch\":0}",
                "Id": 5
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "TrojanCloudAutoBackup",
                "Data": "{\"Switch\":1}",
                "Id": 6
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "UseFullTav",
                "Data": "{\"Switch\":1}",
                "Id": 7
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "HeuristicEngine",
                "Data": "{\"Switch\":1}",
                "Id": 8
            },
            {
                "Modify": 1,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "TrojanCloudGToB",
                "Data": "{\"Switch\":2}",
                "Id": 9
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "RiskScanInfoVirus",
                "Data": "{\"StrictLevel\":\"1\"}",
                "Id": 10
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "RiskScanInfoStartup",
                "Data": "{\"StrictLevel\":\"1\"}",
                "Id": 11
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "RiskScanInfoSetting",
                "Data": "{\"StrictLevel\":\"1\"}",
                "Id": 12
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "RiskScanInfoSoftware",
                "Data": "{\"StrictLevel\":\"1\"}",
                "Id": 13
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "RiskScanInfoPrivacy",
                "Data": "{\"StrictLevel\":\"1\"}",
                "Id": 14
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "RiskScanInfoResidualItem",
                "Data": "{\"StrictLevel\":\"1\"}",
                "Id": 15
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "RiskScanInfoOther",
                "Data": "{\"StrictLevel\":\"1\"}",
                "Id": 16
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "TrojanTrustConfirm",
                "Data": "{\"Switch\":1}",
                "Id": 17
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "TrojanTrustConfirmEnableModify",
                "Data": "{}",
                "Id": 18
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "RestoreQuarantine",
                "Data": "{\"Switch\":1}",
                "Id": 19
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "AddFileFolderTrust",
                "Data": "{\"Switch\":0}",
                "Id": 20
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "QMVirusLibUpdateType",
                "Data": "{\"Day\":1,\"EnableUpdate\":1,\"Hour\":10,\"HourEnd\":17,\"Minute\":0,\"MinuteEnd\":0,\"TimeType\":1,\"UpdateMode\":1}",
                "Id": 21
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 201,
                "Version": 1,
                "Name": "CloudTrustFileOrDir",
                "Data": "{\"ConfigList\":[]}",
                "Id": 22
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 201,
                "Version": 1,
                "Name": "CloudTrustExtension",
                "Data": "{\"ConfigList\":[]}",
                "Id": 23
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 201,
                "Version": 1,
                "Name": "CloudTrustMD5",
                "Data": "{\"ConfigList\":[]}",
                "Id": 24
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 201,
                "Version": 1,
                "Name": "CloudTrustRegistry",
                "Data": "{\"ConfigList\":[]}",
                "Id": 25
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 201,
                "Version": 1,
                "Name": "CloudTrustNetAddr",
                "Data": "{\"ConfigList\":[]}",
                "Id": 26
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 201,
                "Version": 1,
                "Name": "CloudTrustVirusName",
                "Data": "{\"ConfigList\":[]}",
                "Id": 27
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 201,
                "Version": 1,
                "Name": "CloudBlackMD5",
                "Data": "{\"ConfigList\":[]}",
                "Id": 28
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "MultiScanFileType",
                "Data": "{\"Ext\":\"\",\"Switch\":0}",
                "Id": 308
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "UnZipLevel",
                "Data": "{\"Level\":0}",
                "Id": 309
            },
            {
                "Modify": 0,
                "OsType": 0,
                "BusinessId": 200,
                "Version": 1,
                "Name": "TrojanSchedulerFixType",
                "Data": "{\"Switch\":1}",
                "Id": 410
            }
        ]
    }
}
```

