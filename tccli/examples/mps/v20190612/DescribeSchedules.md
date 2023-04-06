**Example 1: 示例**

查询编排ID为0的编排

Input: 

```
tccli mps DescribeSchedules --cli-unfold-argument  \
    --ScheduleIds 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "ScheduleInfoSet": [],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

