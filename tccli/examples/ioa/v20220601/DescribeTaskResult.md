**Example 1: taskresult示例**

查询task执行结果

Input: 

```
tccli ioa DescribeTaskResult --cli-unfold-argument  \
    --Condition.Filters.0.Field abc \
    --Condition.Filters.0.Operator abc \
    --Condition.Filters.0.Values abc \
    --Condition.FilterGroups.0.Filters.0.Field abc \
    --Condition.FilterGroups.0.Filters.0.Operator abc \
    --Condition.FilterGroups.0.Filters.0.Values abc \
    --Condition.Sort.Field abc \
    --Condition.Sort.Order abc \
    --Condition.PageSize 0 \
    --Condition.PageNum 0 \
    --SeqId 0
```

Output: 
```
{
    "Response": {
        "Data": {
            "Page": {
                "PageSize": 1,
                "PageNum": 1,
                "PageCount": 1,
                "Total": 1
            },
            "Items": [
                {
                    "Id": 0,
                    "Name": "abc",
                    "Seq": "abc",
                    "ComputerName": "abc",
                    "Ip": "abc",
                    "Mac": "abc",
                    "GroupId": 0,
                    "GroupName": "abc",
                    "Mid": "abc",
                    "Status": 0,
                    "Result": "abc",
                    "BusinessId": 0,
                    "PushStatus": 0
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

