**Example 1: 人员库升级结果查询**



Input: 

```
tccli iai GetUpgradeGroupFaceModelVersionResult --cli-unfold-argument  \
    --JobId 251007453_upgrade_group_qta_1596529493_gjwh07X7
```

Output: 
```
{
    "Response": {
        "Progress": 100,
        "EndTimestamp": 1596529510000,
        "Status": 1,
        "StartTime": 1596529493217,
        "FromFaceModelVersion": "2.0",
        "GroupId": "100001testGroupUpgrade",
        "FailedFacesUrl": "",
        "ToFaceModelVersion": "3.0",
        "RequestId": "b0835106-e301-4959-90d5-f982007bb4c8"
    }
}
```

