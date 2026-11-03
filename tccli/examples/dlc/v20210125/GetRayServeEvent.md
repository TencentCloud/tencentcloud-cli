**Example 1: 获取RayServe部署事件**



Input: 

```
tccli dlc GetRayServeEvent --cli-unfold-argument  \
    --Id deploy-20260327115134-a1b2 \
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
                "Component": "RayService",
                "Level": "Normal",
                "Message": "Created RayCluster rayserve-xxx"
            }
        ],
        "RequestId": "dffa8e31-2df1-4f61-9e88-df82ec7d7ae8"
    }
}
```

