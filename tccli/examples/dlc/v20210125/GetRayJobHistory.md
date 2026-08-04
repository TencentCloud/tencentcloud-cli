**Example 1: 获取作业状态历史**



Input: 

```
tccli dlc GetRayJobHistory --cli-unfold-argument  \
    --Id rayjob-20260323163852-huvy \
    --Page 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Event": "SUCCESS",
                "FromState": "RUNNING",
                "Id": 639,
                "JobId": "2035999711646846976",
                "ToState": "SUCCEEDED",
                "TransitionTime": 1774256065032
            }
        ],
        "Page": 1,
        "PageSize": 10,
        "Total": 4,
        "TotalPages": 1,
        "RequestId": "dffa8e31-2df1-4f61-9e88-df82ec7d7ae8"
    }
}
```

