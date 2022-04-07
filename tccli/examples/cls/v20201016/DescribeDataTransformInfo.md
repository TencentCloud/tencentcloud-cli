**Example 1: 获取数据加工任务基本信息**



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
                "UpdateTime": "xx",
                "LastEnableTime": "xx",
                "Name": "xx",
                "LogsetId": "xx",
                "SrcTopicName": "xx",
                "SrcTopicId": "xx",
                "DstResources": [
                    {
                        "TopicId": "xx",
                        "Alias": "xx"
                    }
                ],
                "TaskId": "xx",
                "EtlContent": "xx",
                "Type": 0,
                "CreateTime": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

