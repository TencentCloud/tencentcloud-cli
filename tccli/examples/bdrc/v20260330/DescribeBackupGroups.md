**Example 1: 查询实例备份列表**



Input: 

```
tccli bdrc DescribeBackupGroups --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "BackupGroupSet": [
            {
                "AccountName": "",
                "AccountUin": "700002507474",
                "AppId": 260094408,
                "AutoBackupPolicyId": "abp-fys0uzmf",
                "BackupBindDisk": [
                    {
                        "BackupId": "backup-lnlg6z35",
                        "DiskId": "disk-f6wjotd4"
                    }
                ],
                "BackupGroupId": "cbackup-9mge8cx1",
                "BackupGroupName": "auto_ins-kjpsunqm_20260430_00",
                "BackupGroupState": "NORMAL",
                "CreateTime": "2026-04-30T00:15:20+08:00",
                "DeadlineTime": null,
                "InstanceDetails": "{\"Placement\": {\"Zone\": \"ap-guangzhou-2\", \"HostId\": null, \"ProjectId\": 0, \"ProjectName\": \"\\u9ed8\\u8ba4\\u9879\\u76ee\"}, \"InstanceId\": \"ins-kjpsunqm\", \"Uuid\": \"15b65cc6-47b9-4271-a2a4-24552aba54dc\", \"OperatorUin\": \"4611686018428206758\", \"InstanceState\": \"STOPPED\", \"ApplicationRole\": \"\", \"RestrictState\": \"NORMAL\", \"InstanceType\": \"SA9.MEDIUM2\", \"CPU\": 2, \"Memory\": 2, \"InstanceName\": \"FROM cbackup-orpxx9gp\", \"InstanceChargeType\": \"PREPAID\", \"SystemDisk\": {\"DiskType\": \"CLOUD_BSSD\", \"DiskId\": \"disk-f6wjotd4\", \"DiskSize\": 50, \"Encrypt\": false, \"KmsKeyId\": null, \"ThroughputPerformance\": 0, \"CdcId\": null}, \"DataDisks\": [], \"PrivateIpAddresses\": [\"172.16.0.2\"], \"PublicIpAddresses\": null, \"IPv6Addresses\": null, \"InternetAccessible\": {\"InternetMaxBandwidthOut\": 1, \"InternetChargeType\": null}, \"VirtualPrivateCloud\": {\"VpcId\": \"vpc-hj1e0yef\", \"SubnetId\": \"subnet-8hu0ievu\", \"AsVpcGateway\": false, \"VpcName\": \"Default-VPC\", \"SubnetName\": \"Default-Subnet\"}, \"SecurityGroupIds\": [\"sg-kqieqb8n\"], \"LoginSettings\": {\"KeyIds\": null}, \"ImageId\": \"img-6n21msk1\", \"DefaultLoginUser\": \"root\", \"DefaultLoginPort\": 22, \"RenewFlag\": \"NOTIFY_AND_AUTO_RENEW\", \"CreatedTime\": \"2026-04-22T09:57:42Z\", \"ExpiredTime\": \"2026-05-22T09:57:42Z\", \"UnderwriteExpiredTime\": null, \"Tags\": [], \"PlatformProjectId\": null, \"DisasterRecoverGroupId\": \"\", \"DedicatedClusterId\": \"\", \"CamRoleName\": \"\", \"LatestOperation\": \"RollbackInstanceSnapshot\", \"LatestOperationState\": \"SUCCESS\", \"LatestOperationRequestId\": \"3e55411e-ce86-456e-8f17-7a17c41c7d10\", \"IsolatedSource\": \"NOTISOLATED\", \"ChcInstanceType\": \"\", \"HpcClusterId\": \"\", \"DisableApiTermination\": false, \"RdmaIpAddresses\": null, \"VmEniTrunking\": \"off\", \"OsName\": \"TencentOS Server 4 for x86_64\", \"EnableJumboFrame\": false, \"LicenseType\": \"TencentCloud\", \"StopChargingMode\": \"NOT_APPLICABLE\", \"CpuTopology\": {\"ThreadPerCore\": 2, \"CoreCount\": 1}, \"ImageType\": \"PUBLIC_IMAGE\", \"InstanceFamily\": \"SA9\", \"GPU\": 0, \"InnerVpcId\": 11314404, \"DeviceId\": 637560910, \"Architecture\": \"\", \"IsolatedTime\": null, \"IsSafeIsolated\": false, \"SafeIsolatedInfo\": null, \"NewCreationIdentify\": false, \"InstanceClass\": \"S\", \"KeyPairIds\": null, \"OperationMask\": 2002494157813, \"RunFlag\": 4, \"Hypervisor\": 0, \"SwapDisks\": {}, \"LatestOperationErrorMsg\": null, \"BootMode\": \"Legacy BIOS\"}",
                "InstanceId": "ins-kjpsunqm",
                "IsPermanent": false,
                "ModifyTime": "2026-04-30T00:16:31+08:00",
                "Percent": 100,
                "SubAccountUin": "700002507474"
            }
        ],
        "TotalCount": 172,
        "RequestId": "be6a944e-8e47-4a47-a61f-ad448e3a551a"
    }
}
```

