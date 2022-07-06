**Example 1: 运行时访问控制事件列表**



Input: 

```
tccli tcss DescribeAccessControlEvents --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "EventSet": [
            {
                "ContainerName": "xx",
                "ContainerNetSubStatus": "xx",
                "LatestFoundTime": "xx",
                "Status": "xx",
                "Description": "xx",
                "EventType": "xx",
                "EventCount": 0,
                "ImageId": "xx",
                "MatchRuleId": "xx",
                "MatchProcessPath": "xx",
                "Solution": "xx",
                "ProcessName": "xx",
                "ImageName": "xx",
                "Behavior": "xx",
                "MatchFilePath": "xx",
                "ContainerNetStatus": "xx",
                "MatchRuleName": "xx",
                "ContainerStatus": "xx",
                "ContainerId": "xx",
                "FilePath": "xx",
                "MatchAction": "xx",
                "RuleId": "xx",
                "FoundTime": "2020-09-22 00:00:00",
                "FileName": "xx",
                "RuleExist": true,
                "ContainerIsolateOperationSrc": "xx",
                "Id": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

