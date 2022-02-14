**Example 1: 获取项目上报率列表**



Input: 

```
tccli rum DescribeProjectLimits --cli-unfold-argument  \
    --ProjectID 1
```

Output: 
```
{
    "Response": {
        "ProjectLimitSet": [
            {
                "ProjectInterface": "xx",
                "ProjectID": 0,
                "ReportRate": 0,
                "ReportType": 0,
                "ID": 0
            }
        ],
        "RequestId": "xx"
    }
}
```

**Example 2: 获取抽样列表**



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

