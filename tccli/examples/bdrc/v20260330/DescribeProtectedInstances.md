**Example 1: 查询受保护列表信息**



Input: 

```
tccli bdrc DescribeProtectedInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "AgentId": "ins-7630gzfm",
                "AgentStatus": "online",
                "AgentVersion": "2.9.20.1",
                "BackupCount": 26,
                "CreatedTime": "2026-03-26T19:39:11",
                "ExtraInfo": "{\"Placement\": {\"Zone\": \"ap-guangzhou-2\", \"HostId\": null, \"ProjectId\": 0}, \"InstanceId\": \"ins-7630gzfm\", \"Uuid\": \"295eee23-26f1-463c-900c-3a1ba5fe3c7a\", \"OperatorUin\": \"700002520084\", \"InstanceState\": \"RUNNING\", \"ApplicationRole\": \"\", \"RestrictState\": \"NORMAL\", \"InstanceType\": \"SA9.LARGE8\", \"CPU\": 4, \"Memory\": 8, \"InstanceName\": \"\\u672a\\u547d\\u540d\", \"InstanceChargeType\": \"POSTPAID_BY_HOUR\", \"SystemDisk\": {\"DiskType\": \"CLOUD_BSSD\", \"DiskId\": \"disk-8ltp5xeu\", \"DiskSize\": 50, \"Encrypt\": false, \"KmsKeyId\": null, \"ThroughputPerformance\": 0, \"CdcId\": null}, \"DataDisks\": [], \"PrivateIpAddresses\": [\"172.16.16.3\"], \"PublicIpAddresses\": null, \"IPv6Addresses\": null, \"InternetAccessible\": {\"InternetMaxBandwidthOut\": 13, \"InternetChargeType\": null}, \"VirtualPrivateCloud\": {\"VpcId\": \"vpc-5ccfnmj1\", \"SubnetId\": \"subnet-acz7jgvw\", \"AsVpcGateway\": false}, \"SecurityGroupIds\": [\"sg-i3tijpur\"], \"LoginSettings\": {\"KeyIds\": null}, \"ImageId\": \"img-6n21msk1\", \"DefaultLoginUser\": \"root\", \"DefaultLoginPort\": 22, \"RenewFlag\": null, \"CreatedTime\": \"2026-03-26T08:32:29Z\", \"ExpiredTime\": null, \"UnderwriteExpiredTime\": null, \"Tags\": [], \"PlatformProjectId\": null, \"DisasterRecoverGroupId\": \"\", \"DedicatedClusterId\": \"\", \"CamRoleName\": \"cvm-cos\", \"LatestOperation\": \"ModifyInstancesAttribute.CamRoleName\", \"LatestOperationState\": \"SUCCESS\", \"LatestOperationRequestId\": \"cb7a51f0-5084-44b5-9b02-2ed66ef148ea\", \"IsolatedSource\": \"NOTISOLATED\", \"ChcInstanceType\": \"\", \"HpcClusterId\": \"\", \"DisableApiTermination\": false, \"RdmaIpAddresses\": null, \"VmEniTrunking\": \"off\", \"OsName\": \"TencentOS Server 4 for x86_64\", \"EnableJumboFrame\": false, \"LicenseType\": \"TencentCloud\", \"StopChargingMode\": \"NOT_APPLICABLE\", \"CpuTopology\": {\"ThreadPerCore\": 2, \"CoreCount\": 2}, \"ImageType\": \"PUBLIC_IMAGE\", \"InstanceFamily\": \"SA9\", \"LatestOperationErrorMsg\": null, \"BootMode\": \"Legacy BIOS\"}",
                "InstanceId": "ins-7630gzfm",
                "LastHeartbeatTime": "2026-04-01T14:32:13"
            }
        ],
        "RequestId": "30d39f56-3b4f-4818-866e-45d788725744",
        "TotalCount": 1
    }
}
```

