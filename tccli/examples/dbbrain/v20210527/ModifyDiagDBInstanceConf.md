**Example 1: 修改实例巡检状态**



Input: 

```
tccli dbbrain ModifyDiagDBInstanceConf --cli-unfold-argument  \
    --InstanceIds cdb-fyclrp7r \
    --InstanceConfs.DailyInspection Yes \
    --Regions All \
    --Product mysql
```

Output: 
```
{
    "Response": {
        "RequestId": "77db16d7-bbe8-48a7-868b-ed776a96f1ab"
    }
}
```

