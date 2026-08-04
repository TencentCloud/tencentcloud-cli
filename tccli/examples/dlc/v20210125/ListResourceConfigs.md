**Example 1: 列出所有资源配置模板**



Input: 

```
tccli dlc ListResourceConfigs --cli-unfold-argument  \
    --Page 1 \
    --PageSize 100 \
    --StartTime 1771689600000 \
    --EndTime 1774367999000
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AppId": 260090589,
                "CreateTime": 1773911414304,
                "Head": {
                    "HighAvailability": false,
                    "Name": "Head",
                    "PodNum": 1,
                    "ResourceType": "CPU",
                    "Spec": 1
                },
                "Id": "ccbe672e-44be-4518-bcdf-ff85189f7059",
                "Name": "aidanyxu",
                "SubAccountUin": "700002467852",
                "Type": "Ray",
                "Uin": "700002467852",
                "UpdateTime": 1773911414307,
                "Worker": [
                    {
                        "MaxPodNum": 1,
                        "MinPodNum": 1,
                        "Name": "Worker01",
                        "ResourceType": "CPU",
                        "Spec": 1
                    }
                ]
            }
        ],
        "Page": 1,
        "PageSize": 100,
        "Total": 5,
        "TotalPages": 1,
        "RequestId": "c296a82e-6a68-4f67-9edf-e7275635404d"
    }
}
```

