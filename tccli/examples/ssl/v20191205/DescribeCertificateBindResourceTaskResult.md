**Example 1: 查询证书关联云资源结果 **

仅返回总数

Input: 

```
tccli ssl DescribeCertificateBindResourceTaskResult --cli-unfold-argument  \
    --TaskIds 748599
```

Output: 
```
{
    "Response": {
        "SyncTaskBindResourceResult": [
            {
                "TaskId": "748599",
                "BindResourceResult": [
                    {
                        "ResourceType": "clb",
                        "BindResourceRegionResult": [
                            {
                                "Region": "ap-guangzhou",
                                "TotalCount": 1,
                                "Error": ""
                            }
                        ]
                    }
                ],
                "Status": 1,
                "Error": null,
                "CacheTime": "2023-10-12 12:00:00"
            }
        ],
        "RequestId": "d9aa752b-dbd8-49c9-958f-75c051eddfe2"
    }
}
```

