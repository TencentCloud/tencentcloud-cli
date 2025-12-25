**Example 1: 查询版本详情**



Input: 

```
tccli tcbr DescribeVersionDetail --cli-unfold-argument  \
    --EnvId frederickli***clc930f66d \
    --ServerName echos \
    --VersionName echos-008
```

Output: 
```
{
    "Response": {
        "BuildDir": ".",
        "BuildPacks": {
            "BaseImage": "Python3",
            "EntryPoint": "echo 1",
            "LanguageVersion": "",
            "RepoLanguage": "Python",
            "UploadFilename": ""
        },
        "Cmd": "[\"/ap***ho\"]",
        "Cpu": 1,
        "CreatedTime": "2025-12-18 15:32:24",
        "Dockerfile": "",
        "EntryPoint": "[\"/ap***ho\"]",
        "EnvParams": "",
        "LogPath": "stdout",
        "MaxNum": 5,
        "Mem": 2,
        "MinNum": 0,
        "Name": "echos-008",
        "PolicyDetails": [
            {
                "PolicyThreshold": 50,
                "PolicyType": "cpu"
            }
        ],
        "Port": 0,
        "Status": "build_failed",
        "UpdatedTime": "2025-12-18 16:04:43",
        "VolumesConf": [],
        "VpcConf": {
            "SubnetCIDR": "",
            "SubnetId": "",
            "VpcCIDR": "",
            "VpcId": ""
        },
        "RequestId": "1c148a2d-6d44-450e-a160-a097dbf4c63e"
    }
}
```

