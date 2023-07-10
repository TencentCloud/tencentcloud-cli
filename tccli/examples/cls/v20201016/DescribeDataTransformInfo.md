**Example 1: 获取数据加工任务基本信息**

获取数据加工任务基本信息

Input: 

```
tccli cls DescribeDataTransformInfo --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "DataTransformTaskInfos": [
            {
                "Status": 0,
                "EnableFlag": 0,
                "UpdateTime": "2021-08-08 12:12:12",
                "LastEnableTime": "xxxx",
                "Name": "我的加工任务",
                "LogsetId": "xxxx",
                "SrcTopicName": "我的日志主题",
                "SrcTopicId": "61b9XXXX-971a-48c7-984d-ca147cf242c1",
                "DstResources": [
                    {
                        "TopicId": "3d9bXXXX-05a4-4435-ac65-f43e684329b3",
                        "Alias": "别名"
                    }
                ],
                "TaskId": "e4fcXXXX-5e8a-4fe0-b52c-76eeca53e9af",
                "EtlContent": "ields_set()",
                "Type": 0,
                "CreateTime": "2021-08-0712: 12: 12"
            }
        ],
        "RequestId": "6ef60bec-0242-43af-bb20-270359fb54a7"
    }
}
```

