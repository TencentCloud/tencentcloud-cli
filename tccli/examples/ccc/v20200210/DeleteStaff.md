**Example 1: 删除坐席信息示例**



Input: 

```
tccli ccc DeleteStaff --cli-unfold-argument  \
    --SdkAppId 1400692008 \
    --StaffList 1610598376@qq.com
```

Output: 
```
{
    "Response": {
        "DeleteStatusInfo": "Members in OnlineStaffList are online and cannot be deleted",
        "OnlineStaffList": [
            "1610598376@qq.com"
        ],
        "RequestId": "298dca51-0c8b-4efe-aa10-0c7a415089fa"
    }
}
```

