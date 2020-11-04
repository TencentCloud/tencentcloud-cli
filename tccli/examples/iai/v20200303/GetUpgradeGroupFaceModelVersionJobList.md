**Example 1: 获取人员库升级任务列表**



Input: 

```
tccli iai GetUpgradeGroupFaceModelVersionJobList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "JobNum": 1,
        "JobInfos": [
            {
                "JobId": "251007453_upgrade_group_qta_1596529493_gjwh07X7",
                "GroupId": "100001testGroupUpgrade",
                "FromFaceModelVersion": "2.0",
                "ToFaceModelVersion": "3.0",
                "StartTime": 1596529493217,
                "Status": 1
            }
        ],
        "RequestId": "3b035b96-78e8-4330-931d-f976c2850d1b"
    }
}
```

