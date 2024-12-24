**Example 1: 拉取DSPA实例列表**

拉取DSPA实例列表

Input: 

```
tccli dsgc ListDSPAClusters --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name Channel \
    --Filters.0.Values dsgc
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceList": [
            {
                "DspaId": "dpsa-a1b2c3d4",
                "DspaName": "订单分类分级实例",
                "DspaDescription": "上汽集团下级机构",
                "DBAuthCount": 1,
                "CosBindCount": 1,
                "InstanceVersion": "basic",
                "Status": "enabled",
                "ExpiredAt": 1730366388,
                "AppId": 125500778,
                "TrialVersion": "trial-standard",
                "TrialEndAt": 0,
                "DbTotalQuota": 3,
                "CosTotalQuota": 3,
                "CosQuotaUnit": "T",
                "RenewFlag": 1,
                "Channel": "wedata",
                "InsAuthCount": 0,
                "InsTotalQuota": 0
            }
        ],
        "DenyAll": true,
        "RequestId": "18dafbf7-83d5-4159-aeaf-4a02f1975176"
    }
}
```

