**Example 1: 查询拨测分地区数据**



Input: 

```
tccli teo DescribeSpeedTestingDetails --cli-unfold-argument  \
    --ZoneId zone-cdafdasdf
```

Output: 
```
{
    "Response": {
        "SpeedTestingDetailData": {
            "ZoneName": "tencent.com",
            "DistrictStatistics": [
                {
                    "Alpha2": "AF",
                    "LoadTime": 30
                }
            ],
            "ZoneId": "zone-cdafdasdf"
        },
        "RequestId": "084d5612-67a7-4aca-aac9-827aa3662b2d"
    }
}
```

