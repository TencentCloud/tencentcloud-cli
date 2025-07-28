**Example 1: 创建月度制备份策略。**

创建一个名字为plan1的备份策略，每个月的1/2号的凌晨1点至2点进行数据备份，并且数据文件保留40天。

Input: 

```
tccli postgres CreateBackupPlan --cli-unfold-argument  \
    --PlanName plan1 \
    --BackupPeriodType month \
    --DBInstanceId postgres-kwk4tq23 \
    --MinBackupStartTime 01:00:00 \
    --MaxBackupStartTime 02:00:00 \
    --BackupPeriod 1 2 \
    --BaseBackupRetentionPeriod 40
```

Output: 
```
{
    "Response": {
        "RequestId": "8a61e500-aa33-454c-9ec2-da2a368c39ab",
        "PlanId": "dfea3bb4-8ca7-5e79-aefb-9d231f2b66b6"
    }
}
```

