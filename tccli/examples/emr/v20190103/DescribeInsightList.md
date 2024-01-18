**Example 1: 获取洞察信息**



Input: 

```
tccli emr DescribeInsightList --cli-unfold-argument  \
    --InstanceId emr-d82w3t9p \
    --PageSize 10 \
    --StartTime 1701792000 \
    --EndTime 1701878399 \
    --Page 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 9,
        "RequestId": "12345678999",
        "ResultList": [
            {
                "ScheduleTaskName": "",
                "RuleID": "HIVE-ScanManyPartition",
                "ScheduleTaskExecID": "",
                "ScheduleFlowName": "",
                "Detail": "easechen_dw.test_orc big scan",
                "Value": 0,
                "RuleExplain": "扫描分区数超过表总分区80%",
                "Suggestion": "添加分区扫描条件",
                "RuleName": "HIVE-大表扫描",
                "JobConf": "",
                "Type": "HIVE",
                "ID": "hadoop_20231206140857_1bbd81e2-b752-424b-aa61-a811a40c3099"
            }
        ]
    }
}
```

