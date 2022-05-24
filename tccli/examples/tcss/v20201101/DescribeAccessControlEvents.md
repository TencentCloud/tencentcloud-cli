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
                "Status": "xx",
                "ContainerName": "xx",
                "ContainerId": "xx",
                "MatchRuleName": "xx",
                "EventType": "xx",
                "MatchAction": "xx",
                "FilePath": "xx",
                "Solution": "xx",
                "FoundTime": "2020-09-22 00:00:00",
                "FileName": "xx",
                "ProcessName": "xx",
                "MatchProcessPath": "xx",
                "ImageName": "xx",
                "Behavior": "xx",
                "MatchRuleId": "xx",
                "ImageId": "xx",
                "MatchFilePath": "xx",
                "Id": "xx",
                "LatestFoundTime": "2020-09-22 00:00:00",
                "EventCount": 0,
                "RuleExist": true,
                "Description": "xx",
                "RuleId": "xx",
                "ContainerIsolateOperationSrc": "xx",
                "ContainerNetSubStatus": "xx",
                "ContainerNetStatus": "xx"
            }
        ],
        "TotalCount": 1,
        "RequestId": "xx"
    }
}
```

