**Example 1: 查询维护时间窗口**

查询维护时间窗口

Input: 

```
tccli vdb DescribeInstanceMaintenanceWindow --cli-unfold-argument  \
    --InstanceId vdb-bmz0****
```

Output: 
```
{
    "Response": {
        "EndTime": "03:00",
        "InstanceId": "vdb-bmz0****",
        "RequestId": "19265be4-5202-4740-a7b8-5ab602eb3677",
        "StartTime": "00:00",
        "TimeSpan": 3
    }
}
```

