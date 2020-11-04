**Example 1: 查询考勤结果**

查询考勤结果

Input: 

```
tccli tci DescribeAttendanceResult --cli-unfold-argument  \
    --JobId 549
```

Output: 
```
{
    "Response": {
        "RequestId": "03262329-3567-4e9c-9049-7e9b60f83dd3",
        "Progress": 100,
        "AttendanceSet": [
            {
                "PersonId": "33944418",
                "Face": {
                    "Ts": 862640,
                    "Similarity": 0.9369908,
                    "SnapshotUrl": "http://attendance-pictures-1255701415.cos.ap-guangzhou.myqcloud.com/attendance/74973491_33944418_1616_800_78_95_1554975659.jpg?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDEOuBIhv4wHI2ChdxFbnngLxbrzpUGo8H%26q-sign-time%3D1554975659%3B1557567659%26q-key-time%3D1554975659%3B1557567659%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D71ce55bb682b1a853ca596538eab2435061fe155"
                }
            },
            {
                "PersonId": "36736596",
                "Face": {
                    "Ts": 104080,
                    "Similarity": 0.97687095,
                    "SnapshotUrl": "http://attendance-pictures-1255701415.cos.ap-guangzhou.myqcloud.com/attendance/74214931_36736596_1167_1_60_75_1554974891.jpg?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDEOuBIhv4wHI2ChdxFbnngLxbrzpUGo8H%26q-sign-time%3D1554974891%3B1557566891%26q-key-time%3D1554974891%3B1557566891%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D4434d8381f9d2dac6e3cda05860390d85d7cc905"
                }
            }
        ],
        "SuspectedSet": [
            {
                "PersonId": "37218264",
                "FaceSet": [
                    {
                        "Ts": 261560,
                        "Similarity": 0.89789367,
                        "SnapshotUrl": "http://attendance-pictures-1255701415.cos.ap-guangzhou.myqcloud.com/attendance/74372411_37218264_737_447_57_66_1554974946.jpg?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDEOuBIhv4wHI2ChdxFbnngLxbrzpUGo8H%26q-sign-time%3D1554974946%3B1557566946%26q-key-time%3D1554974946%3B1557566946%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D6606a82a704d288b6752af74d1cb70207842100f"
                    },
                    {
                        "Ts": 473040,
                        "Similarity": 0.8813029,
                        "SnapshotUrl": "http://attendance-pictures-1255701415.cos.ap-guangzhou.myqcloud.com/attendance/74583891_37218264_761_380_66_74_1554975022.jpg?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDEOuBIhv4wHI2ChdxFbnngLxbrzpUGo8H%26q-sign-time%3D1554975022%3B1557567022%26q-key-time%3D1554975022%3B1557567022%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3Da55b9bcdba20dcc51c3c19b7da608c8279cbf7f1"
                    },
                    {
                        "Ts": 218360,
                        "Similarity": 0.82336843,
                        "SnapshotUrl": "http://attendance-pictures-1255701415.cos.ap-guangzhou.myqcloud.com/attendance/74329211_37218264_791_418_56_68_1554974930.jpg?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDEOuBIhv4wHI2ChdxFbnngLxbrzpUGo8H%26q-sign-time%3D1554974931%3B1557566931%26q-key-time%3D1554974931%3B1557566931%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3De60ab62375cdde7ad73f00448c8c69b1e39494e4"
                    }
                ]
            }
        ],
        "AbsenceSet": null
    }
}
```

