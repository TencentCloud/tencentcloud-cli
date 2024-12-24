**Example 1: 添加上线云应用版本请求**



Input: 

```
tccli car SetApplicationVersionOnline --cli-unfold-argument  \
    --ApplicationId app-glheghe \
    --ApplicationVersionId ver-cebgkd
```

Output: 
```
{
    "Response": {
        "Versions": [
            {
                "ApplicationVersionId": "ver-855fr3i4",
                "ApplicationVersionName": "steamvr",
                "ApplicationVersionRegions": [
                    "ap-chinese-mainland"
                ],
                "ApplicationVersionSize": 5612961473,
                "ApplicationVersionStatus": "Usable",
                "ApplicationVersionUpdateMode": "",
                "CreateTime": "2023-05-25T09:22:10Z"
            },
            {
                "ApplicationVersionId": "ver-qi5inuk4",
                "ApplicationVersionName": "test",
                "ApplicationVersionRegions": [
                    "ap-chinese-mainland"
                ],
                "ApplicationVersionSize": 1978592076,
                "ApplicationVersionStatus": "Inuse",
                "ApplicationVersionUpdateMode": "",
                "CreateTime": "2024-07-25T10:39:57Z"
            }
        ],
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

