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
                "ContainerId": "xx",
                "ContainerName": "xx",
                "EventType": "xx",
                "Solution": "xx",
                "FoundTime": "2020-09-22 00:00:00",
                "LatestFoundTime": "2020-09-22 00:00:00",
                "ImageId": "xx",
                "EventName": "xx",
                "ImageName": "xx",
                "PodName": "xx",
                "Description": "xx",
                "EventCount": 0,
                "NodeName": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

