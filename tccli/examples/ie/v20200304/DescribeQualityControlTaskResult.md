**Example 1: 查询媒体质检任务结果**



Input: 

```
tccli ie DescribeQualityControlTaskResult --cli-unfold-argument  \
    --TaskId 1260170830789492736
```

Output: 
```
{
    "Response": {
        "TaskResult": {
            "TaskId": "488022239",
            "Status": 2,
            "ErrCode": 0,
            "ErrMsg": "",
            "Progress": 100,
            "UsedTime": 51,
            "Duration": 150,
            "QualityEvaluationScore": 74,
            "JitterResults": [
                {
                    "QualityControlItems": [
                        {
                            "StartTimeOffset": 93.92,
                            "EndTimeOffset": 111.16,
                            "Confidence": 100
                        },
                        {
                            "StartTimeOffset": 113.16,
                            "EndTimeOffset": 130.248,
                            "Confidence": 100
                        }
                    ]
                }
            ]
        },
        "RequestId": "request_id_query"
    }
}
```

