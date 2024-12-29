**Example 1: 查询节点数据盘信息**



Input: 

```
tccli emr DescribeNodeDataDisks --cli-unfold-argument  \
    --InstanceId emr-xxxxxxx \
    --CvmInstanceIds ins-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "CBSList": [
            {
                "DeleteWithInstance": true,
                "DiskChargeType": "POSTPAID_BY_HOUR",
                "DiskId": "disk-xxxxxxxx",
                "DiskName": "未命名_1",
                "DiskSize": 100,
                "DiskState": "ATTACHED",
                "DiskType": "CLOUD_SSD",
                "DiskUsage": "DATA_DISK",
                "DeadlineTime": ""
            },
            {
                "DeleteWithInstance": true,
                "DiskChargeType": "POSTPAID_BY_HOUR",
                "DiskId": "disk-xxxxxxxx",
                "DiskName": "未命名_0",
                "DiskSize": 50,
                "DiskState": "ATTACHED",
                "DiskType": "CLOUD_SSD",
                "DiskUsage": "SYSTEM_DISK",
                "DeadlineTime": ""
            }
        ],
        "RequestId": "9dd6b795-aed5-4a09-b493-f460c1f1a0c5",
        "TotalCount": 2
    }
}
```

