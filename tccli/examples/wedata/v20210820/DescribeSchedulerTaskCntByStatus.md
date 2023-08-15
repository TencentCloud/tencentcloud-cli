**Example 1: 示例1**

demo

Input: 

```
tccli wedata DescribeSchedulerTaskCntByStatus --cli-unfold-argument  \
    --ProjectId 12312
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CountTag": 1,
                "TotalNum": 1,
                "RunningNum": 1,
                "StoppingNum": 1,
                "StoppedNum": 1,
                "FrozenNum": 1,
                "YearNum": 1,
                "MonthNum": 1,
                "WeekNum": 1,
                "DayNum": 1,
                "HourNum": 1,
                "MinuteNum": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: 1**

1

Input: 

```
tccli wedata DescribeSchedulerTaskCntByStatus --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "AuthFailure.SignatureFailure",
            "Message": "The provided credentials could not be validated. Please check your signature is correct."
        },
        "RequestId": "ffa95942-29bb-4bfd-b207-a23d4c265504"
    }
}
```

