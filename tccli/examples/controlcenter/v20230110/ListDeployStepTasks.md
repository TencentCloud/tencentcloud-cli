**Example 1: 示例**

通过基线identifier获取部署任务历史

Input: 

```
tccli controlcenter ListDeployStepTasks --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0 \
    --Identifier TCC-AF_CAM_USER_PASSWORD_POLICY
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "BaselineDeployStepTaskList": [
            {
                "TaskId": "s8gsj834y8ef0cjs",
                "Identifier": "TCC-AF_CAM_USER_PASSWORD_POLICY",
                "MemberUin": 100000000001,
                "Status": "Success",
                "Output": "",
                "ErrCode": "Ok",
                "ErrMessage": "Ok",
                "CreateTime": "2022-08-18 12:00:00",
                "UpdateTime": "2022-08-18 12:00:00"
            }
        ],
        "RequestId": "ef0e0140-4e51-4087-95a1-f7fd18ca6d63"
    }
}
```

