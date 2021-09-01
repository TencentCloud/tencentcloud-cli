**Example 1: 查询伸缩组活动**



Input: 

```
tccli tiems DescribeRsgAsGroupActivities --cli-unfold-argument  \
    --Id asg-xxxxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "206bf53c-c658-44cb-b50a-5eb9904c49fd",
        "RsgAsGroupActivitySet": [
            {
                "Id": "asa-xxxxxxxx",
                "RsgAsGroupId": "asg-xxxxxxxx",
                "ActivityType": "SCALE_OUT",
                "StatusCode": "FAILED",
                "StatusMessage": "选择的机型在当前可用区已售罄",
                "Cause": "因匹配期望实例数",
                "Description": "因匹配期望实例数，扩容1台",
                "StartTime": "2019-12-30T10:11:26+08:00",
                "EndTime": "2019-12-30T10:11:27+08:00",
                "CreateTime": "2019-12-30T10:11:26+08:00",
                "StatusMessageSimplified": "云主机售罄"
            }
        ],
        "TotalCount": 1
    }
}
```

