**Example 1: 实例一**



Input: 

```
tccli tcb DescribeCloudBaseRunPodList --cli-unfold-argument  \
    --EnvId "test" \
    --ServerName "test" \
    --VersionName "test-001" \
    --PodName "test-001-111" \
    --Status "running"
```

Output: 
```
{
    "Response": {
        "PodList": [
            {
                "Webshell": "https://tkecache.cloud.tencent.com/qcloud/ccs/webconsole/index.html#rid=4&clusterId=cls-e7ovytqu&podId=test-nanking-30-001-5d54476cf-zzkzc&containerName=test-nanking-30-001&namespace=default&tkeeks=1",
                "PodId": "test-nanking-30-001-5d54476cf-zzkzc",
                "Status": "Running",
                "PodIp": "10.0.0.36",
                "CreateTime": "2020-06-30 13:28:33 +0000 UTC"
            }
        ],
        "TotalCount": 1,
        "Offset": 0,
        "RequestId": "8971182b-32a0-4d9b-b0e2-2190524a1cfb",
        "Limit": 10
    }
}
```

