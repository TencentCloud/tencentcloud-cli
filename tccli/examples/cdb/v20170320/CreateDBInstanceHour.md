**Example 1: 发货**



Input: 

```
tccli cdb CreateDBInstanceHour --cli-unfold-argument  \
    --GoodsNum 1 \
    --Memory 1000 \
    --Volume 150 \
    --EngineVersion 8.0 \
    --UniqVpcId vpc-xxxxxx \
    --UniqSubnetId subnet-xxxxxx \
    --ProjectId 0 \
    --Zone 540001 \
    --InstanceRole master \
    --Port 3306 \
    --ParamList.0.Name lower_case_table_names \
    --ParamList.0.Value 1 \
    --ProtectMode 1 \
    --DeployMode 0 \
    --SlaveZone 540001 \
    --BackupZone 0 \
    --SecurityGroup sg-xxxxx \
    --InstanceName xxxxxxx \
    --AlarmPolicyList -1 \
    --Cpu 1 \
    --ParamTemplateType HIGH_STABILITY \
    --EngineType InnoDB \
    --DestroyProtect off
```

Output: 
```
{
    "Response": {
        "DealIds": [
            "20260330601111111111"
        ],
        "InstanceIds": [
            "cdb-xxxzz"
        ],
        "RequestId": "d30a3795-ee9e-4dc7-bf93-1e7ab751b6f5"
    }
}
```

