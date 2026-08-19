**Example 1: 获取最近一次立即检测任务信息**



Input: 

```
tccli csip DescribeLastScanTaskInfo --cli-unfold-argument  \
    --TaskSource asset
```

Output: 
```
{
    "Response": {
        "TaskInfo": {
            "Progress": 0,
            "ScanTime": "",
            "Status": "",
            "TaskID": ""
        },
        "RequestId": "e2f5f5ef-d16e-4441-9959-621bbc0e55b1"
    }
}
```

