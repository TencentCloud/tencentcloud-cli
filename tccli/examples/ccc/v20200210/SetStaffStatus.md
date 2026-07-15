**Example 1: 设置座席状态**



Input: 

```
tccli ccc SetStaffStatus --cli-unfold-argument  \
    --SdkAppId 1400692008 \
    --StaffStatusList.0.StaffUserId weijuny***nt.com \
    --StaffStatusList.0.Status free \
    --StaffStatusList.0.Reason huiyi
```

Output: 
```
{
    "Response": {
        "StaffStatusList": [
            {
                "ErrorCode": "",
                "ErrorMessage": "",
                "PreviousReason": "",
                "PreviousStatus": "rest",
                "Reason": "huiyi",
                "StaffUserId": "weijuny***nt.com",
                "Status": "free"
            }
        ],
        "RequestId": "6980f29d-c779-4a49-bf65-736bfc3b76a0"
    }
}
```

