**Example 1: 调用示例**



Input: 

```
tccli csip DescribeBaselineMainTaskList --cli-unfold-argument  \
    --MemberId mem-tencent-6*************29 \
    --Limit 10 \
    --Offset 1 \
    --Order asc \
    --By ID
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Appid": 200000000,
                "CheckAssetType": "HOST",
                "ErrCode": "",
                "ErrMessage": "",
                "FinishTime": "2026-07-27T19:10:32Z",
                "ID": 268,
                "JobID": "e4f1e274665c0fbd2eacdcfccb8fd1d5",
                "ScanFailedCount": 4,
                "ScanSuccessCount": 5,
                "ScanTotalCount": 9,
                "Solution": "",
                "StartTime": "2026-07-27T19:00:00Z",
                "Status": "SUCCESS",
                "TaskType": "PERIODIC"
            }
        ],
        "TotalCount": 281,
        "RequestId": "162e5f18-d260-4908-86a0-e86b91c7c1f7"
    }
}
```

