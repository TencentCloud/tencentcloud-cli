**Example 1: 专家服务-安全管家列表**

专家服务-安全管家列表

Input: 

```
tccli cwp DescribeEmergencyResponseList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "TaskId": "cve2021-1616989795566545881",
                "HostNum": 1,
                "Status": 1,
                "StartTime": "2021-03-29 12:49:55",
                "EndTime": "--",
                "ReportPath": ""
            },
            {
                "TaskId": "cve2021-1617009909259811227",
                "HostNum": 1,
                "Status": 0,
                "StartTime": "--",
                "EndTime": "--",
                "ReportPath": ""
            }
        ],
        "RequestId": "48ca3c70-801e-48b1-80a7-1007afbf5ffb",
        "TotalCount": 2
    }
}
```

