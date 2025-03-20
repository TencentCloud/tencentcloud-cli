**Example 1: 查询风险容器镜像列表**



Input: 

```
tccli tcss DescribeEventEscapeImageList --cli-unfold-argument  \
    --Limit 1 \
    --Offset 1 \
    --Filters.0.Name EventType \
    --Filters.0.Values MOUNT_SENSITIVE_PTAH \
    --Filters.0.ExactMatch True \
    --Order asc \
    --By Status
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "ImageId": "sha256:9aae1601d6832af6c69ef257f09",
                "EventType": "local",
                "OriginEventType": "MOUNT_SENSITIVE_PTAH",
                "UniqueKey": "1398abd1-98x71134",
                "ImageName": "centos-7.6",
                "ContainerCount": 0,
                "FoundTime": "2020-09-22 00:00:00",
                "LatestFoundTime": "2020-09-22 00:00:00",
                "EventCount": 0,
                "Status": "EVENT_INGNORE",
                "Description": "Description",
                "Solution": "Solution"
            }
        ],
        "TotalCount": 1,
        "RequestId": "dc56fda9-58c8-4c4f-9e8c-b7296836c1fe"
    }
}
```

