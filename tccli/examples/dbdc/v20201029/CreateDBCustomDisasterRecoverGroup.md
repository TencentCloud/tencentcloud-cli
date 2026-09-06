**Example 1: 创建置放群组**



Input: 

```
tccli dbdc CreateDBCustomDisasterRecoverGroup --cli-unfold-argument  \
    --Name 置放群组测试 \
    --Type HOST \
    --Strategy SPREAD \
    --Affinity 5
```

Output: 
```
{
    "Response": {
        "CreatedTime": "2026-08-27T08:24:28Z",
        "CurrentNum": 0,
        "DisasterRecoverGroupId": "dbps-81aqu2cs",
        "Name": "置放群组测试",
        "NodeQuotaTotal": 50,
        "Status": "Creating",
        "Strategy": "SPREAD",
        "Type": "HOST",
        "RequestId": "1d913863-86cd-4d18-b071-27f5ef2781bd"
    }
}
```

