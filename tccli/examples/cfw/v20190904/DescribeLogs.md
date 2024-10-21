**Example 1: 日志审计日志查询**

日志审计日志查询

Input: 

```
tccli cfw DescribeLogs --cli-unfold-argument  \
    --Filters.0.Name protocol \
    --Filters.0.Values ANY TCP ICMP \
    --Filters.0.OperatorType 1 \
    --Limit 10 \
    --Offset 0 \
    --Index netflow_border \
    --StartTime 2021-09-21 12:00:00 \
    --EndTime 2021-09-21 12:00:00
```

Output: 
```
{
    "Response": {
        "Data": "[{\"StartTime\":\"2024-09-21 12:00:00\",\"EndTime\":\"2024-09-21 12:01:00\",\"SourceIp\":\"91.148.190.158\",\"TargetIp\":\"81.70.48.154\",\"SourcePort\":\"50865\",\"TargetPort\":\"17589\",\"Direction\":\"1\",\"Domain\":\"\",\"Protocol\":\"TCP\",\"Address\":\"保加利亚索非亚州索非亚\",\"Supplier\":\"Tamatiya EOOD\",\"AssetName\":\"\",\"ReceivePackageNum\":1,\"ReceiveBytesNum\":44,\"SendPackageNum\":0,\"SendBytesNum\":0,\"FlowPackageNum\":1,\"FlowBytesNum\":44,\"AssetId\":\"\",\"Tags\":\"\"},{\"StartTime\":\"2024-09-21 12:00:00\",\"EndTime\":\"2024-09-21 12:00:11\",\"SourceIp\":\"80.64.30.109\",\"TargetIp\":\"81.70.41.63\",\"SourcePort\":\"42573\",\"TargetPort\":\"38847\",\"Direction\":\"1\",\"Domain\":\"\",\"Protocol\":\"TCP\",\"Address\":\"俄罗斯莫斯科\",\"Supplier\":\"Hivelocity Inc\",\"AssetName\":\"\",\"ReceivePackageNum\":2,\"ReceiveBytesNum\":80,\"SendPackageNum\":1,\"SendBytesNum\":40,\"FlowPackageNum\":3,\"FlowBytesNum\":120,\"AssetId\":\"\",\"Tags\":\"\"},{\"StartTime\":\"2024-09-21 12:00:00\",\"EndTime\":\"2024-09-21 12:01:00\",\"SourceIp\":\"91.148.190.158\",\"TargetIp\":\"81.70.48.154\",\"SourcePort\":\"50865\",\"TargetPort\":\"17589\",\"Direction\":\"1\",\"Domain\":\"\",\"Protocol\":\"TCP\",\"Address\":\"保加利亚索非亚州索非亚\",\"Supplier\":\"Tamatiya EOOD\",\"AssetName\":\"league-规则测试靶机-勿删\",\"ReceivePackageNum\":1,\"ReceiveBytesNum\":44,\"SendPackageNum\":0,\"SendBytesNum\":0,\"FlowPackageNum\":1,\"FlowBytesNum\":44,\"AssetId\":\"ins-mec2asax\",\"Tags\":\"\"},{\"StartTime\":\"2024-09-21 12:00:00\",\"EndTime\":\"2024-09-21 12:00:11\",\"SourceIp\":\"89.248.165.16\",\"TargetIp\":\"81.70.41.63\",\"SourcePort\":\"52015\",\"TargetPort\":\"38433\",\"Direction\":\"1\",\"Domain\":\"\",\"Protocol\":\"TCP\",\"Address\":\"荷兰北荷兰省阿姆斯特丹\",\"Supplier\":\"IP Volume inc\",\"AssetName\":\"\",\"ReceivePackageNum\":2,\"ReceiveBytesNum\":88,\"SendPackageNum\":1,\"SendBytesNum\":40,\"FlowPackageNum\":3,\"FlowBytesNum\":128,\"AssetId\":\"\",\"Tags\":\"\"},{\"StartTime\":\"2024-09-21 12:00:00\",\"EndTime\":\"2024-09-21 12:00:11\",\"SourceIp\":\"80.64.30.109\",\"TargetIp\":\"81.70.41.63\",\"SourcePort\":\"42573\",\"TargetPort\":\"38847\",\"Direction\":\"1\",\"Domain\":\"\",\"Protocol\":\"TCP\",\"Address\":\"俄罗斯莫斯科\",\"Supplier\":\"Hivelocity Inc\",\"AssetName\":\"ins-r0jh352d\",\"ReceivePackageNum\":2,\"ReceiveBytesNum\":80,\"SendPackageNum\":1,\"SendBytesNum\":40,\"FlowPackageNum\":3,\"FlowBytesNum\":120,\"AssetId\":\"ins-r0jh352d\",\"Tags\":\"\"},{\"StartTime\":\"2024-09-21 12:00:00\",\"EndTime\":\"2024-09-21 12:00:11\",\"SourceIp\":\"89.248.165.16\",\"TargetIp\":\"81.70.41.63\",\"SourcePort\":\"52015\",\"TargetPort\":\"38433\",\"Direction\":\"1\",\"Domain\":\"\",\"Protocol\":\"TCP\",\"Address\":\"荷兰北荷兰省阿姆斯特丹\",\"Supplier\":\"IP Volume inc\",\"AssetName\":\"ins-r0jh352d\",\"ReceivePackageNum\":2,\"ReceiveBytesNum\":88,\"SendPackageNum\":1,\"SendBytesNum\":40,\"FlowPackageNum\":3,\"FlowBytesNum\":128,\"AssetId\":\"ins-r0jh352d\",\"Tags\":\"\"}]",
        "RequestId": "e368c536-0331-46d3-b888-90c27152970f",
        "ReturnCode": 0,
        "ReturnMsg": "success",
        "Total": 0
    }
}
```

