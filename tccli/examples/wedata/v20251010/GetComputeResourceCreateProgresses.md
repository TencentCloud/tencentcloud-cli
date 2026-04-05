**Example 1: 获取计算资源创建进度**



Input: 

```
tccli wedata GetComputeResourceCreateProgresses --cli-unfold-argument  \
    --WorkspaceId 1820764929296400 \
    --ResourceId cr-f8d9e7c6b5a4
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": 2,
            "CreateTime": "1770024383000",
            "EstimatedTime": 0,
            "OverallProgress": 100,
            "Name": "Engine creation",
            "Progresses": [
                {
                    "Name": "Start Create",
                    "Progress": 100,
                    "StartTime": "1770024385000",
                    "EndTime": "1770024385000",
                    "Status": 2
                },
                {
                    "Name": "Creating Network Resources",
                    "Progress": 100,
                    "StartTime": "1770024387000",
                    "EndTime": "1770024398000",
                    "Status": 2,
                    "EstimatedTime": 11
                },
                {
                    "Name": "Creating Computing Resources",
                    "Progress": 100,
                    "StartTime": "1770024398000",
                    "EndTime": "1770034189000",
                    "Status": 2,
                    "EstimatedTime": 9791
                }
            ]
        },
        "RequestId": "99b40499-626f-4460-9b1d-f6f89752ac99"
    }
}
```

