**Example 1: 升级实例内核大版本**

实例当前大版本号为10，需要使用PostgreSQL 15的相关特性，则可以通过大版本升级功能将实例的内核版本从10升级到15，并在指定时间窗内执行升级。

Input: 

```
tccli postgres UpgradeDBInstanceMajorVersion --cli-unfold-argument  \
    --DBInstanceId postgres-qwe12k98 \
    --TargetDBKernelVersion v15.1_r1.6 \
    --UpgradeCheck False \
    --BackupBeforeUpgrade True \
    --StatisticsRefreshOption 0 \
    --ExtensionUpgradeOption 0 \
    --UpgradeTimeOption 1 \
    --UpgradeTimeBegin 01:00:00 \
    --UpgradeTimeEnd 02:00:00
```

Output: 
```
{
    "Response": {
        "RequestId": "93b86d2d-0d4e-4c83-9322-70f45b039012"
    }
}
```

