**Example 1: DescribeVersionDetail**



Input: 

```
tccli tcbr DescribeVersionDetail --cli-unfold-argument  \
    --EnvId fisher-pr***c0df14561 \
    --ServerName test-cls \
    --VersionName test-cls-003 \
    --Channel gateway
```

Output: 
```
{
    "Response": {
        "BuildDir": ".",
        "Cmd": "[*",
        "Cpu": 0.25,
        "CreatedTime": "2025-10-15 16:27:04",
        "Dockerfile": "Dockerfile",
        "EntryPoint": "[*",
        "EnvParams": "",
        "LogPath": "stdout",
        "MaxNum": 5,
        "Mem": 0.5,
        "MinNum": 0,
        "Name": "test-cls-003",
        "PolicyDetails": [
            {
                "PolicyThreshold": 60,
                "PolicyType": "cpu"
            }
        ],
        "Port": 0,
        "Status": "deploy_failed",
        "UpdatedTime": "2025-10-15 16:30:37",
        "VolumesConf": [],
        "VpcConf": {
            "SubnetCIDR": "",
            "SubnetId": "",
            "VpcCIDR": "",
            "VpcId": ""
        },
        "RequestId": "d3b7befc-5afe-4aa8-8a5e-7aa9efa6c3c0"
    }
}
```

