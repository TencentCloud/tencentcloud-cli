**Example 1: getescapeInfo**



Input: 

```
tccli tcss DescribeEscapeEventInfo --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "EventSet": [
            {
                "Status": "xx",
                "EventId": "xx",
                "HostID": "xx",
                "ContainerId": "xx",
                "ContainerName": "xx",
                "EventType": "xx",
                "EventCount": 0,
                "Solution": "xx",
                "FoundTime": "2020-09-22 00:00:00",
                "ImageId": "xx",
                "EventName": "xx",
                "ImageName": "xx",
                "Description": "xx",
                "PodName": "xx",
                "NodeIP": "xx",
                "LatestFoundTime": "2020-09-22 00:00:00",
                "NodeName": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

