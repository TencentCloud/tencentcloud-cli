**Example 1: 拉取DSPA实例列表**

拉取DSPA实例列表

Input: 

```
tccli dsgc ListDSPAClusters --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "InstanceList": [
            {
                "DspaId": "abc",
                "DspaName": "abc",
                "DspaDescription": "abc",
                "DBAuthCount": 1,
                "CosBindCount": 1,
                "InstanceVersion": "abc",
                "Status": "abc",
                "ExpiredAt": 1,
                "AppId": 1,
                "TrialVersion": "abc",
                "TrialEndAt": 1,
                "DbTotalQuota": 0,
                "CosTotalQuota": 0,
                "RenewFlag": 1
            }
        ],
        "DenyAll": true,
        "RequestId": "abc"
    }
}
```

