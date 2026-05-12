**Example 1: 查询日志备份配置**

查询日志备份配置

Input: 

```
tccli csip DescribeDspmBackupSetting --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "BackupLogSaveTime": 0,
        "RestoreLogSaveTime": 0,
        "LogMaxSaveTime": 180,
        "OnlineLogMaxSaveTime": 30,
        "RequestId": "qwedaexczcqwe"
    }
}
```

