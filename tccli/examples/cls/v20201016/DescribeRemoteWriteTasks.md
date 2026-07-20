**Example 1: 获取RemoteWrite投递任务列表**



Input: 

```
tccli cls DescribeRemoteWriteTasks --cli-unfold-argument  \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "AuthInfo": null,
                "AuthType": 0,
                "CreateTime": "2023-09-07 11:16:50",
                "Enable": 1,
                "LogsetId": "e1111113-e816-4ae8-a8f7-edde0e2fc963",
                "Name": "111111111",
                "NetType": 1,
                "RemoteWriteURL": "http://10.2.10.27:8080/api/v1/write",
                "Status": 3,
                "Target": "Prometheus",
                "TaskId": "a2d1111-afae-467e-8816-0bc405283bec",
                "TopicId": "376011111-76e0-48c7-bfff-018afc9bca48",
                "UpdateTime": "2024-10-30 21:01:35",
                "VirtualGatewayType": 0,
                "VpcId": "vpc-11111"
            }
        ],
        "RequestId": "e02371b7-5ef0-4ae7-8a33-f703b9d5f564",
        "TotalCount": 6
    }
}
```

