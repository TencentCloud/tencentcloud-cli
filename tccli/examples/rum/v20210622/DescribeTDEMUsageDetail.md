**Example 1: 查询用量明细**



Input: 

```
tccli rum DescribeTDEMUsageDetail --cli-unfold-argument  \
    --StartTime 2026-09-15 00:00:00 \
    --EndTime 2026-09-22 13:00:00 \
    --Keyword ****测试	 \
    --Offset 0 \
    --Limit 100
```

Output: 
```
{
    "Response": {
        "DetailSet": [
            {
                "AppId": "17",
                "AppName": "*********",
                "AppStatus": 2,
                "AppType": "electron",
                "ByDate": [
                    {
                        "ReportVolume": 0,
                        "Time": "2026-09-15 00:00:00"
                    }
                ],
                "InstanceId": "rum-jqtz5UaeVyXZ",
                "InstanceName": "测试环境测试",
                "InstanceStatus": 2,
                "Percent": 88.67616164561716,
                "ReportVolume": 3782902
            }
        ],
        "ReportVolume": 4265974,
        "TotalCount": 13,
        "RequestId": "eb103256-daa6-4e89-a36a-3c0fb226fec5"
    }
}
```

