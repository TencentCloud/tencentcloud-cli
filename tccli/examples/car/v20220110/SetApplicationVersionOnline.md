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
                "ApplicationVersionId": "ver-cebgkd",
                "ApplicationVersionSize": 1024,
                "ApplicationVersionStatus": "Inuse",
                "ApplicationVersionName": "xxx",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ApplicationVersionRegions": [
                    "ap-tokyo"
                ]
            },
            {
                "ApplicationVersionId": "ver-grshefa",
                "ApplicationVersionSize": 2048,
                "ApplicationVersionStatus": "Usable",
                "ApplicationVersionName": "xxx",
                "CreateTime": "2020-09-22T00:00:00+00:00",
                "ApplicationVersionRegions": [
                    "ap-tokyo"
                ]
            }
        ],
        "RequestId": "4eb17e58-68da-4e9a-b298-0894723c9022"
    }
}
```

