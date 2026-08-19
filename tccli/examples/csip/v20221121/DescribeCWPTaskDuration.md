**Example 1: 获取任务下发预估时长**

获取任务下发预估时长

Input: 

```
tccli csip DescribeCWPTaskDuration --cli-unfold-argument  \
    --UuidCnt 1000
```

Output: 
```
{
    "Response": {
        "Duration": 10,
        "RequestId": "dacb16ef-285c-41d0-8f05-cbfb5a59a696"
    }
}
```

