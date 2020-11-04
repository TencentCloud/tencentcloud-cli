**Example 1: 查询用户的告警主题列表**



Input: 

```
tccli cat DescribeAlarmTopic --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Topics": [
            {
                "TopicId": "topic-82pr09bv8z",
                "TopicName": "云拨测默认主题"
            }
        ],
        "RequestId": "80912aeb-d68e-4a3d-a8a4-af791073a275"
    }
}
```

