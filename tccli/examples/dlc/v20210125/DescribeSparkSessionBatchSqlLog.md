**Example 1: 查询Spark SQL批任务日志**

查询Spark SQL批任务日志

Input: 

```
tccli dlc DescribeSparkSessionBatchSqlLog --cli-unfold-argument  \
    --BatchId d3018ad4-9a7e-4f64-a3f4-f38507c69742
```

Output: 
```
{
    "Response": {
        "State": 0,
        "LogSet": [
            {
                "Step": "BEG",
                "Time": "2023-03-20 12:12:12",
                "Message": "集群名称",
                "Operate": [
                    {
                        "Text": "dateEngine-1",
                        "Operate": "COPY",
                        "Supplement": [
                            {
                                "Key": "TASKID",
                                "Value": "d0ds1sad4-9d7e-4f64-a3f4-f385dcs6742"
                            }
                        ]
                    }
                ]
            }
        ],
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

