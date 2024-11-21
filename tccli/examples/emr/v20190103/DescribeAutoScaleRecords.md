**Example 1: 获取弹性扩缩容历史示例**



Input: 

```
tccli emr DescribeAutoScaleRecords --cli-unfold-argument  \
    --InstanceId emr-3ap64zl6 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RecordList": [
            {
                "ActionStatus": "SUCCESS",
                "ActionTime": "2024-11-05 19:38:10",
                "CompensateCount": 0,
                "CompensateFlag": 0,
                "EndTime": "2024-11-05 19:38:37",
                "ExpectScaleNum": 1,
                "RetryCount": 0,
                "RetryInfo": "重试次数: 0\n重试结束时间: 0000-00-00 00:00:00\n重试原因: ",
                "ScaleAction": "SCALE_IN",
                "ScaleInfo": "缩容信息:[缩容前:11台, 缩容后:10台, 成功:1台, 失败:0台]",
                "SpecInfo": "1台: 可用区: 南京3区\nSA2.LARGE8: CPU: 4核 内存:8GB\n\t系统盘:\n \t\t通用型SSD云硬盘: 50G\n\t数据盘:\n\t\t增强型SSD云硬盘: 100G x 1\n\n",
                "StrategyName": "回归-re04",
                "StrategyType": 1
            }
        ],
        "RequestId": "8ad457bc-16ca-4ed5-af21-3ed4b58d719b",
        "TotalCount": 70
    }
}
```

