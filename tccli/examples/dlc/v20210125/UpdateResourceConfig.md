**Example 1: 更新资源配置模板**



Input: 

```
tccli dlc UpdateResourceConfig --cli-unfold-argument  \
    --Id ccbe672e-44be-4518-bcdf-ff85189f7059 \
    --Name aidanyxu \
    --Head.Name Head \
    --Head.PodNum 1 \
    --Head.HighAvailability False \
    --Head.ResourceType CPU \
    --Head.Spec 1 \
    --Worker.0.Name Worker01 \
    --Worker.0.MinPodNum 1 \
    --Worker.0.MaxPodNum 1 \
    --Worker.0.ResourceType CPU \
    --Worker.0.Spec 1 \
    --Type Ray
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
        "UpdateTime": 1774340769148,
        "Worker": [
            {
                "MaxPodNum": 1,
                "MinPodNum": 1,
                "Name": "Worker01",
                "ResourceType": "CPU",
                "Spec": 1
            }
        ],
        "RequestId": "0d303c32-9f2f-491c-9a13-5f60b21d4325"
    }
}
```

