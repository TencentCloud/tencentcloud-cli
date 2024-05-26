**Example 1: 修改实例巡检状态**

修改实例巡检状态。

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

**Example 2: 修改Redis实例大key周期性分析**

开启Redis实例大key周期性分析并自定义分隔符。

Input: 

```
tccli dbbrain ModifyDiagDBInstanceConf --cli-unfold-argument  \
    --Product redis \
    --Regions All \
    --InstanceIds crs-pz1raq11 \
    --InstanceConfs.AnalysisTopKey Yes \
    --InstanceConfs.KeyDelimiters _ - :
```

Output: 
```
{
    "Response": {
        "RequestId": "bcd97ab0-16d1-11ef-8e52-3d11a9997f13"
    }
}
```

