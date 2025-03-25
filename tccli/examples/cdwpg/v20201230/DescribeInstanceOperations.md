**Example 1: 获取集群操作列表**

获取集群操作列表

Input: 

```
tccli cdwpg DescribeInstanceOperations --cli-unfold-argument  \
    --InstanceId cdwpg-rzshdeh1 \
    --Offset 0 \
    --Limit 1 \
    --StartTime 2025-03-01 12:12:12 \
    --EndTime 2025-03-24 12:12:12
```

Output: 
```
{
    "Response": {
        "Operations": [
            {
                "Action": "创建",
                "Context": "{\"AppID\":130108xxxx3,\"Uin\":\"100xxx695507\",\"OperateUin\":\"1000264xxxx545\",\"Region\":\"ap-chongqing\",\"Zone\":\"ap-chongqing-1\",\"Resources\":[{\"Type\":\"cn\",\"SpecName\":\"S_4_16_H_CN\",\"Count\":2,\"DiskSpec\":{\"DiskType\":\"CLOUD_HSSD\",\"DiskSize\":200,\"DiskCount\":1}},{\"Type\":\"dn\",\"SpecName\":\"S_4_16_H\",\"Count\":2,\"DiskSpec\":{\"DiskType\":\"CLOUD_HSSD\",\"DiskSize\":20,\"DiskCount\":10}}],\"UserVPCID\":\"vpc-1asw4o73\",\"UserSubnetID\":\"subnet-rdlodajk\",\"Version\":\"3.16.9.4\",\"ImageID\":\"img-m4wwu8tr\",\"StackID\":\"NULL\",\"InstanceName\":\"hugogao_test\",\"InstanceType\":\"TbaseV3\",\"InstanceID\":\"cdwpg-rzshdeh1\",\"AdminPassword\":\"Y2R3MUAzNDU=\",\"ResourceAppID\":1305504398,\"ResourceUin\":\"10001xxx92051\",\"ResourceOperateUin\":\"100018xxx51\",\"SecurityGroupID\":\"sg-2ndss7x8se\",\"Case\":\"create_instance\",\"Tags\":{\"ResourceTags\":null},\"ExpiredTime\":\"0000.00.00 00:00:00\",\"Kind\":\"external_resource_user\",\"ChargeProperties\":{\"ChargeType\":\"POSTPAID_BY_HOUR\",\"RenewFlag\":0,\"TimeSpan\":1,\"TimeUnit\":\"h\"},\"Kms\":{\"KmsId\":\"\",\"KmsRegion\":\"\",\"KmsStatus\":false},\"DealName\":\"\",\"Language\":\"zh-CN\",\"Recovery\":{\"RecoveryTimePoint\":\"\",\"RecoveryTime\":\"\",\"RecoveryInstanceId\":\"\"},\"SyncTypePair\":{\"SyncType\":2,\"NgroupSrmode\":2,\"DataReliable\":false},\"Charset\":\"UTF8\",\"UpgradeId\":0,\"ManualBackup\":\"\",\"RSs\":null,\"RecoverNodeIp\":\"\"}",
                "StartTime": "2025-03-19 16:37:38",
                "EndTime": "2025-03-19 16:47:35",
                "Id": 222931,
                "InstanceId": "cdwpg-rzshdeh1",
                "Status": 2,
                "Uin": "100026473545",
                "UpdateTime": "2025-03-19 16:47:35"
            }
        ],
        "RequestId": "6410f499-5599-48ef-8f12-884a84219a24",
        "TotalCount": 1
    }
}
```

