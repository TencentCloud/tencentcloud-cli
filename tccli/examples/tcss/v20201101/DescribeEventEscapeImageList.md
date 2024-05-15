**Example 1: 查询风险容器镜像列表**



Input: 

```
tccli tcss DescribeEventEscapeImageList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1 \
    --Filters.0.Name abc \
    --Filters.0.Values abc \
    --Filters.0.ExactMatch True \
    --Order abc \
    --By abc
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "EventType": "abc",
                "OriginEventType": "abc",
                "ImageName": "abc",
                "ContainerCount": 0,
                "FoundTime": "2020-09-22 00:00:00",
                "LatestFoundTime": "2020-09-22 00:00:00",
                "EventCount": 0,
                "Status": "abc",
                "Description": "abc",
                "Solution": "abc"
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

