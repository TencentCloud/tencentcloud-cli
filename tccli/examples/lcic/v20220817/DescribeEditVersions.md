**Example 1: 获取当前可以全部版本信息**



Input: 

```
tccli lcic DescribeEditVersions --cli-unfold-argument  \
    --SdkAppId 3520371 \
    --RoomId 326744409
```

Output: 
```
{
    "Response": {
        "ClassId": 326744409,
        "LatestVersionNo": 2,
        "MainVersion": 2,
        "Versions": [
            {
                "CreatedAtMs": 0,
                "CreatorUserId": "",
                "FailReason": "",
                "IsMain": false,
                "IsSource": true,
                "KeepDurationSec": 0,
                "Status": "READY",
                "Version": 1
            }
        ],
        "RequestId": "25cb9f60-9f9a-4152-9523-232a482c041e"
    }
}
```

