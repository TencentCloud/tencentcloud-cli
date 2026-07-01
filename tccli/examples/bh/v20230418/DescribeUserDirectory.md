**Example 1: 获取用户目录**



Input: 

```
tccli bh DescribeUserDirectory --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "UserDirSet": [
            {
                "AutoSync": true,
                "CreateTime": "2026-06-24T09:57:23+08:00",
                "DirId": 899412,
                "DirName": "test_ioa",
                "Id": 4294967478,
                "NextSyncTime": "2026-07-01T10:00:00+08:00",
                "Source": 0,
                "SourceName": "自建账户",
                "SyncCron": "00 10 * * 3",
                "UserOrgSet": [
                    {
                        "BindGroupIds": [],
                        "OrgId": 900790,
                        "OrgIdPath": "819729.899412.900790",
                        "OrgName": "test_ioa_01",
                        "OrgNamePath": "全网账户.test_ioa.test_ioa_01",
                        "UserTotal": 1
                    }
                ],
                "UserTotal": 23
            }
        ],
        "RequestId": "8c8368b5-c4a0-4778-8f4a-1866b0667933"
    }
}
```

