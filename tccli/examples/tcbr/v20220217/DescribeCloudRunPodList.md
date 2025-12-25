**Example 1: success 0630**



Input: 

```
tccli tcbr DescribeCloudRunPodList --cli-unfold-argument  \
    --EnvId esdfsdf \
    --ServerName server \
    --VersionName versfsdf \
    --PageSize 0 \
    --PageNum 0
```

Output: 
```
{
    "Response": {
        "PodList": [
            {
                "Webshell": "",
                "PodId": "sdfsdf",
                "Status": "running",
                "CreateTime": "2025-07-25 19:00:00"
            }
        ],
        "TotalCount": 0,
        "RequestId": "sdfsdfdf"
    }
}
```

