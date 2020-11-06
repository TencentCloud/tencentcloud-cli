**Example 1: 获取专业版周报列表**

获取专业版周报列表

Input: 

```
tccli cwp DescribeWeeklyReports --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "WeeklyReports": [
            {
                "BeginDate": "2018-10-08",
                "EndDate": "2018-10-14"
            }
        ],
        "TotalCount": 10
    }
}
```

