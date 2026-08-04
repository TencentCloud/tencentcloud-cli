**Example 1: 获取资源配置模板详情**



Input: 

```
tccli dlc GetResourceConfig --cli-unfold-argument  \
    --Id ccbe672e-44be-4518-bcdf-ff85189f7059
```

Output: 
```
{
    "Response": {
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
        ],
        "RequestId": "8c49161d-cdc9-4015-ad5c-941217089ef0"
    }
}
```

