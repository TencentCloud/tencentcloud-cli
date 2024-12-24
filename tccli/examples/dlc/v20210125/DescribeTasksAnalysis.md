**Example 1: 洞察分析列表**



Input: 

```
tccli dlc DescribeTasksAnalysis --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "580668d5-d47c-44a1-86ea-273843d94778",
        "TaskList": [
            {
                "Id": "67ea3d23b70611efbc745254006dc901",
                "State": 2,
                "SQL": "select * from tpcds_sql_orc.store_sales limit 100000",
                "DataEngineName": "super_spark_270",
                "InstanceStartTime": 1733842361290,
                "InstanceCompleteTime": 1733842401892,
                "JobTimeSum": 35589,
                "TaskTimeSum": 403,
                "InputRecordsSum": 49049600,
                "InputBytesSum": 20648020108,
                "OutputRecordsSum": 100000,
                "OutputBytesSum": 14638477,
                "ShuffleReadBytesSum": 0,
                "ShuffleReadRecordsSum": 0,
                "AnalysisStatus": "[\"SPARK-OutputSmallFile\"]"
            }
        ],
        "TotalCount": 1
    }
}
```

