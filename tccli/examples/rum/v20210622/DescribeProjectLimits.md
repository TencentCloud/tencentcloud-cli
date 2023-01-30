**Example 1: 获取应用上报抽样信息**

获取应用上报抽样信息

Input: 

```
tccli rum DescribeProjectLimits --cli-unfold-argument  \
    --ProjectID 8
```

Output: 
```
{
    "Response": {
        "ProjectLimitSet": [
            {
                "ID": 17,
                "ProjectID": 8,
                "ProjectInterface": "web",
                "ReportRate": 10,
                "ReportType": 1
            }
        ],
        "RequestId": "6f867613-843d-410a-8000-c74477ca48a8"
    }
}
```

