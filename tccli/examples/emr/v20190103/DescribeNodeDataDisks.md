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
                "Attached": true,
                "DeadlineTime": "",
                "DeleteWithInstance": true,
                "DifferDaysOfDeadline": 0,
                "DiskChargeType": "POSTPAID_BY_HOUR",
                "DiskId": "disk-bpcm1kg4",
                "DiskName": "emr-Master.1_emr-gzpmy487_数据盘_1",
                "DiskSize": 200,
                "DiskState": "ATTACHED",
                "DiskType": "CLOUD_HSSD",
                "DiskUsage": "DATA_DISK",
                "InstanceId": "ins-4y5u591o",
                "InstanceIdList": [
                    "ins-4y5u591o"
                ],
                "RenewFlag": "",
                "Shareable": false
            }
        ],
        "RequestId": "e681bb5e-e0b9-49ba-b3bd-be504a76e91b",
        "TotalCount": 1
    }
}
```

