**Example 1: 获取作业事件**



Input: 

```
tccli dlc GetRayJobEvent --cli-unfold-argument  \
    --Id rayjob-20260323163852-huvy \
    --StartTime 1774256000000 \
    --EndTime 1774259600000
```

Output: 
```
{
    "Response": {
        "Context": "eyJvZmZzZXQiOjEwfQ==",
        "ListOver": false,
        "Events": [
            {
                "EventTime": 1774256065032,
                "Component": "RayJob",
                "Level": "Normal",
                "Message": "Created RayCluster rayjob-xxx"
            }
        ],
        "RequestId": "dffa8e31-2df1-4f61-9e88-df82ec7d7ae8"
    }
}
```

