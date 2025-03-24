**Example 1: 查看客户可用的服务器型号列表**



Input: 

```
tccli chc DescribeAvailableModelList --cli-unfold-argument  \
    --IdcId 373 \
    --DeviceType server
```

Output: 
```
{
    "Response": {
        "ModelVersionSet": [
            {
                "DevHeight": "2",
                "DeviceType": "server",
                "ModelVersion": "SFT1502-III-V1"
            },
            {
                "DevHeight": "30",
                "DeviceType": "server",
                "ModelVersion": "lhshen server test 03-V1"
            },
            {
                "DevHeight": "2",
                "DeviceType": "server",
                "ModelVersion": "DELL R740-T1-V1"
            },
            {
                "DevHeight": "2",
                "DeviceType": "server",
                "ModelVersion": "Dell R740-T001-V1"
            },
            {
                "DevHeight": "4",
                "DeviceType": "server",
                "ModelVersion": "LD-002-V1"
            },
            {
                "DevHeight": "2",
                "DeviceType": "server",
                "ModelVersion": "LD-SERVER-001-V1"
            },
            {
                "DevHeight": "23",
                "DeviceType": "server",
                "ModelVersion": "BM X3650 M5003-V1"
            },
            {
                "DevHeight": "22",
                "DeviceType": "server",
                "ModelVersion": "IBM X3650 M5007-V1"
            },
            {
                "DevHeight": "69",
                "DeviceType": "server",
                "ModelVersion": "lihwli0217001-V2"
            },
            {
                "DevHeight": "23",
                "DeviceType": "server",
                "ModelVersion": "234-V1"
            },
            {
                "DevHeight": "1",
                "DeviceType": "server",
                "ModelVersion": "QW LD003 V1-V1"
            },
            {
                "DevHeight": "1",
                "DeviceType": "server",
                "ModelVersion": "QW LD003 V2-V1"
            },
            {
                "DevHeight": "23",
                "DeviceType": "server",
                "ModelVersion": "lihwli02250001-V1"
            },
            {
                "DevHeight": "11",
                "DeviceType": "server",
                "ModelVersion": "lhshen-test-V1"
            }
        ],
        "RequestId": "5bc61ca8-aa3c-4307-a239-873fbb8e5b18"
    }
}
```

