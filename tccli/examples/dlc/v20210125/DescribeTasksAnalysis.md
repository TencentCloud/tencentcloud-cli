**Example 1: 洞察分析列表**



Input: 

```
tccli dlc DescribeTasksAnalysis --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TaskList": [
            {
                "Id": "abc",
                "InstanceStartTime": 0,
                "InstanceCompleteTime": 0,
                "State": 0,
                "SQL": "abc",
                "DataEngineName": "abc",
                "JobTimeSum": 0,
                "TaskTimeSum": 0,
                "InputRecordsSum": 0,
                "InputBytesSum": 0,
                "OutputRecordsSum": 0,
                "OutputBytesSum": 0,
                "ShuffleReadBytesSum": 0,
                "ShuffleReadRecordsSum": 0,
                "AnalysisStatus": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

