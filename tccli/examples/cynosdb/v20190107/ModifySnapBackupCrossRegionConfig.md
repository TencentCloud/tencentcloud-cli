**Example 1: 修改快照备份跨地域配置**

Modify Snap Backup Cross Region Config

Input: 

```
tccli cynosdb ModifySnapBackupCrossRegionConfig --cli-unfold-argument  \
    --ClusterId cynosdbmysql-gfo7ejhl \
    --CrossRegionsEnable OFF
```

Output: 
```
{
    "Response": {
        "RequestId": "be38b494-263a-45f7-b6f3-ecbd66ac65bb",
        "TaskId": 49297
    }
}
```

