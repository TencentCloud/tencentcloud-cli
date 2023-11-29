**Example 1: 查询开关列表接口示例**

获取容器日志组件开关信息

Input: 

```
tccli tke DescribeLogSwitches --cli-unfold-argument  \
    --ClusterType tke \
    --ClusterIds cls-dpla09lf cls-oh0o9d8f cls-9r7hfd5h
```

Output: 
```
{
    "Response": {
        "RequestId": "bd5b2352-8900-4ab7-b79b-2f51f2e92c26",
        "SwitchSet": [
            {
                "Audit": {
                    "Enable": false,
                    "LogsetId": "",
                    "TopicId": "",
                    "TopicRegion": "",
                    "UpgradeAble": false,
                    "Version": ""
                },
                "ClusterId": "cls-oh0o9d8f",
                "Event": {
                    "Enable": false,
                    "LogsetId": "",
                    "TopicId": "",
                    "TopicRegion": "",
                    "UpgradeAble": false,
                    "Version": ""
                },
                "Log": {
                    "Enable": false,
                    "LogsetId": "",
                    "TopicId": "",
                    "TopicRegion": "",
                    "UpgradeAble": false,
                    "Version": ""
                },
                "MasterLog": {
                    "Enable": false,
                    "LogsetId": "",
                    "TopicId": "",
                    "TopicRegion": "",
                    "UpgradeAble": false,
                    "Version": ""
                }
            },
            {
                "Audit": {
                    "Enable": true,
                    "LogsetId": "d12706e7-ae3b-42cf-9dab-d41e71482193",
                    "TopicId": "77b6130b-81cf-46dc-9faf-8d4b5afca77f",
                    "TopicRegion": "ap-chengdu",
                    "UpgradeAble": false,
                    "Version": ""
                },
                "ClusterId": "cls-dpla09lf",
                "Event": {
                    "Enable": true,
                    "LogsetId": "d12706e7-ae3b-42cf-9dab-d41e71482193",
                    "TopicId": "ec5a1f8e-5234-419b-bf10-e5789e325bdf",
                    "TopicRegion": "ap-chengdu",
                    "UpgradeAble": false,
                    "Version": ""
                },
                "Log": {
                    "Enable": true,
                    "LogsetId": "",
                    "TopicId": "",
                    "TopicRegion": "",
                    "UpgradeAble": false,
                    "Version": "1.1.14"
                },
                "MasterLog": {
                    "Enable": false,
                    "LogsetId": "",
                    "TopicId": "",
                    "TopicRegion": "",
                    "UpgradeAble": false,
                    "Version": ""
                }
            },
            {
                "Audit": {
                    "Enable": true,
                    "LogsetId": "299ec2db-8139-4f4c-8f83-6022e427df65",
                    "TopicId": "72d439f2-befa-47cb-924b-39c2d7a64d0b",
                    "TopicRegion": "ap-chengdu",
                    "UpgradeAble": false,
                    "Version": ""
                },
                "ClusterId": "cls-9r7hfd5h",
                "Event": {
                    "Enable": true,
                    "LogsetId": "299ec2db-8139-4f4c-8f83-6022e427df65",
                    "TopicId": "20408e26-932a-4400-a0c8-c5874669265b",
                    "TopicRegion": "ap-chengdu",
                    "UpgradeAble": false,
                    "Version": ""
                },
                "Log": {
                    "Enable": true,
                    "LogsetId": "",
                    "TopicId": "",
                    "TopicRegion": "",
                    "UpgradeAble": false,
                    "Version": "1.1.14"
                },
                "MasterLog": {
                    "Enable": false,
                    "LogsetId": "",
                    "TopicId": "",
                    "TopicRegion": "",
                    "UpgradeAble": false,
                    "Version": ""
                }
            }
        ]
    }
}
```

