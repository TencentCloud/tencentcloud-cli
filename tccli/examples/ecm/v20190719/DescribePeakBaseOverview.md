**Example 1: 查询概览页基础数据**

查询概览页基础数据

Input: 

```
tccli ecm DescribePeakBaseOverview --cli-unfold-argument  \
    --StartTime 2020-09-04 \
    --EndTime 2020-09-04
```

Output: 
```
{
    "Response": {
        "RequestId": "d043adf2-ee74-418a-a1a5-5c63a052b481",
        "PeakFamilyInfoSet": [
            {
                "InstanceFamily": {
                    "InstanceFamilyTypeName": "标准型S4",
                    "InstanceFamilyType": "S4"
                },
                "PeakBaseSet": [
                    {
                        "PeakCpuNum": 8018,
                        "RecordTime": "2020-09-04 00:00:00",
                        "PeakMemoryNum": 16044,
                        "PeakStorageNum": 90676
                    },
                    {
                        "PeakCpuNum": 8018,
                        "RecordTime": "2020-09-04 01:00:00",
                        "PeakMemoryNum": 16044,
                        "PeakStorageNum": 90676
                    },
                    {
                        "PeakCpuNum": 8018,
                        "RecordTime": "2020-09-04 02:00:00",
                        "PeakMemoryNum": 16044,
                        "PeakStorageNum": 90676
                    },
                    {
                        "PeakCpuNum": 8018,
                        "RecordTime": "2020-09-04 03:00:00",
                        "PeakMemoryNum": 16044,
                        "PeakStorageNum": 90676
                    },
                    {
                        "PeakCpuNum": 8018,
                        "RecordTime": "2020-09-04 04:00:00",
                        "PeakMemoryNum": 16044,
                        "PeakStorageNum": 90676
                    },
                    {
                        "PeakCpuNum": 8018,
                        "RecordTime": "2020-09-04 05:00:00",
                        "PeakMemoryNum": 16044,
                        "PeakStorageNum": 90676
                    },
                    {
                        "PeakCpuNum": 8018,
                        "RecordTime": "2020-09-04 06:00:00",
                        "PeakMemoryNum": 16044,
                        "PeakStorageNum": 90676
                    },
                    {
                        "PeakCpuNum": 8018,
                        "RecordTime": "2020-09-04 07:00:00",
                        "PeakMemoryNum": 16044,
                        "PeakStorageNum": 90676
                    }
                ]
            },
            {
                "InstanceFamily": {
                    "InstanceFamilyTypeName": "标准型SN3ne",
                    "InstanceFamilyType": "SN3ne"
                },
                "PeakBaseSet": [
                    {
                        "PeakCpuNum": 433,
                        "RecordTime": "2020-09-04 00:00:00",
                        "PeakMemoryNum": 882,
                        "PeakStorageNum": 5529
                    },
                    {
                        "PeakCpuNum": 433,
                        "RecordTime": "2020-09-04 01:00:00",
                        "PeakMemoryNum": 882,
                        "PeakStorageNum": 5529
                    },
                    {
                        "PeakCpuNum": 433,
                        "RecordTime": "2020-09-04 02:00:00",
                        "PeakMemoryNum": 882,
                        "PeakStorageNum": 5529
                    },
                    {
                        "PeakCpuNum": 433,
                        "RecordTime": "2020-09-04 03:00:00",
                        "PeakMemoryNum": 882,
                        "PeakStorageNum": 5529
                    },
                    {
                        "PeakCpuNum": 433,
                        "RecordTime": "2020-09-04 04:00:00",
                        "PeakMemoryNum": 882,
                        "PeakStorageNum": 5529
                    },
                    {
                        "PeakCpuNum": 433,
                        "RecordTime": "2020-09-04 05:00:00",
                        "PeakMemoryNum": 882,
                        "PeakStorageNum": 5529
                    },
                    {
                        "PeakCpuNum": 433,
                        "RecordTime": "2020-09-04 06:00:00",
                        "PeakMemoryNum": 882,
                        "PeakStorageNum": 5529
                    },
                    {
                        "PeakCpuNum": 433,
                        "RecordTime": "2020-09-04 07:00:00",
                        "PeakMemoryNum": 882,
                        "PeakStorageNum": 5529
                    }
                ]
            }
        ]
    }
}
```

