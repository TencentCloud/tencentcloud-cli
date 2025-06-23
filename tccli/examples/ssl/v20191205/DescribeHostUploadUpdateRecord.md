**Example 1: 查询证书云资源更新（证书ID不变）记录列表**



Input: 

```
tccli ssl DescribeHostUploadUpdateRecord --cli-unfold-argument  \
    --OldCertificateId OMhKAc35
```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "DeployRecordList": [
            {
                "Id": 3,
                "OldCertId": "OMhKAc35",
                "ResourceTypes": [
                    "clb"
                ],
                "Status": 0,
                "CreateTime": "2025-05-27 12:05:26",
                "UpdateTime": "2025-05-27 12:05:26"
            },
            {
                "Id": 2,
                "OldCertId": "OMhKAc35",
                "ResourceTypes": [
                    "clb"
                ],
                "Status": 7,
                "CreateTime": "2025-05-26 18:05:38",
                "UpdateTime": "2025-05-26 18:45:12"
            },
            {
                "Id": 1,
                "OldCertId": "OMhKAc35",
                "ResourceTypes": [
                    "clb"
                ],
                "Status": 4,
                "CreateTime": "2025-05-26 12:51:43",
                "UpdateTime": "2025-05-26 17:51:43"
            }
        ],
        "RequestId": "79b4dae4-51a7-4345-9b2b-0c6a29f69291"
    }
}
```

