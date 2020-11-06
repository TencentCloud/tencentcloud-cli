**Example 1: 查询触发器日志**



Input: 

```
tccli tcr DescribeWebhookTriggerLog --cli-unfold-argument  \
    --RegistryId tcr-ak9876 \
    --Namespace someNs \
    --Id 9
```

Output: 
```
{
    "Response": {
        "RequestId": "be17f554-32fd-451c-a1cd-64f9bd164e3f",
        "TotalCount": 3,
        "Logs": [
            {
                "Id": 2,
                "TriggerId": 25,
                "EventType": "pushImage",
                "NotifyType": "http",
                "Status": "finished",
                "Detail": "{\"type\":\"pushImage\",\"occur_at\":1586774843,\"event_data\":{\"resources\":[{\"digest\":\"sha256:7ac7819e1523911399b798309025935a9968b277d86d50e5255465d6592c0266\",\"tag\":\"v1\",\"resource_url\":\"wcctest.tencentcloudcr.com/nginx/nginx:v1\"}],\"repository\":{\"date_created\":1586777885,\"name\":\"nginx\",\"namespace\":\"nginx\",\"repo_full_name\":\"nginx/nginx\",\"repo_type\":\"public\"}},\"operator\":\"3211064422\"}",
                "CreationTime": "2020-04-14T02:47:23.177329+08:00",
                "UpdateTime": "2020-04-14T02:47:24.244664+08:00"
            }
        ]
    }
}
```

