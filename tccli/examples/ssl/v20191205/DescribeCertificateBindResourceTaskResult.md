**Example 1: 查询证书关联云资源结果 **

仅返回总数

Input: 

```
tccli ssl DescribeCertificateBindResourceTaskResult --cli-unfold-argument  \
    --TaskIds abc
```

Output: 
```
{
    "Response": {
        "SyncTaskBindResourceResult": [
            {
                "TaskId": "abc",
                "BindResourceResult": [
                    {
                        "ResourceType": "abc",
                        "BindResourceRegionResult": [
                            {
                                "Region": "abc",
                                "TotalCount": 1
                            }
                        ]
                    }
                ],
                "Status": 1,
                "Error": {
                    "Code": "abc",
                    "Message": "abc"
                },
                "CacheTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

