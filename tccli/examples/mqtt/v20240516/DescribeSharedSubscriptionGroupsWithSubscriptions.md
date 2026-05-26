**Example 1: 示例**



Input: 

```
tccli mqtt DescribeSharedSubscriptionGroupsWithSubscriptions --cli-unfold-argument  \
    --InstanceId mqtt-b843q2px
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "CreateTime": 1778488384000,
                "SharedName": "group1",
                "TopicFilters": [
                    "home/room1"
                ],
                "UpdateTime": 1778488384000
            }
        ],
        "TotalCount": 3,
        "RequestId": "28ad3ec0-81b5-4cfc-8dc8-6fb00f7936a7"
    }
}
```

