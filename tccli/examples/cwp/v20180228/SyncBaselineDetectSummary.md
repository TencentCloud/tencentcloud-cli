**Example 1: 同步检测概要**



Input: 

```
tccli cwp SyncBaselineDetectSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "DetectingTaskIds": [
            2379
        ],
        "EndTime": "",
        "HostCount": 1,
        "LeftMins": 3,
        "NotPassPolicyCount": 19,
        "ProgressRate": 20,
        "RequestId": "69fce851-ee60-44ac-8ab1-62c2c7856051",
        "StartTime": "2022-08-23 15:07:02",
        "WillFirstScan": 0
    }
}
```

**Example 2: 指定任务ID概要请求**

指定任务ID概要请求

Input: 

```
tccli cwp SyncBaselineDetectSummary --cli-unfold-argument  \
    --TaskIds 299 298
```

Output: 
```
{
    "Response": {
        "DetectingTaskIds": [],
        "EndTime": "2023-12-25 12:05:27",
        "HostCount": 31,
        "LeftMins": 0,
        "NotPassPolicyCount": 1,
        "ProgressRate": 100,
        "RequestId": "5f862bd8-6931-45ee-a5d9-0fe2c4ea30d7",
        "StartTime": "2023-12-25 09:36:00",
        "WillFirstScan": 0
    }
}
```

