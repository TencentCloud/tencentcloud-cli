**Example 1: DescribeCloudRunServerDetail**



Input: 

```
tccli tcbr DescribeCloudRunServerDetail --cli-unfold-argument  \
    --EnvId prod-2g59lad002c864a6 \
    --ServerName golang-h7yv
```

Output: 
```
{
    "Response": {
        "BaseInfo": {
            "AccessTypes": [],
            "CustomDomainName": "",
            "CustomDomainNames": [],
            "DefaultDomainName": "https://golang-h7yv-121864-6-1258467748.sh.run.tcloudbase.com",
            "ServerName": "golang-h7yv",
            "Status": "running",
            "UpdateTime": "2024-09-13 10:31:56"
        },
        "OnlineVersionInfos": [
            {
                "FlowRatio": "100",
                "ImageUrl": "ccr.ccs.tencentyun.com/weixincloud/weixincloud_golang:10",
                "VersionName": "golang-h7yv-001"
            }
        ],
        "RequestId": "ec98425e-cc3f-4c95-a231-cd144757c9bd",
        "ServerConfig": {
            "BuildDir": "",
            "Cpu": 1,
            "CreateTime": "2024-09-13 10:31:17",
            "CustomLogs": "stdout",
            "Dockerfile": "Dockerfile",
            "EnvId": "prod-2g59lad002c864a6",
            "EnvParams": "",
            "HasDockerfile": false,
            "InitialDelaySeconds": 2,
            "LogParseType": "",
            "LogSetId": "",
            "LogTopicId": "",
            "LogType": "",
            "MaxNum": 5,
            "Mem": 2,
            "MinNum": 0,
            "OpenAccessTypes": [],
            "PolicyDetails": [
                {
                    "PolicyThreshold": 60,
                    "PolicyType": "cpu"
                },
                {
                    "PolicyThreshold": 60,
                    "PolicyType": "mem"
                }
            ],
            "Port": 8080,
            "ServerName": "golang-h7yv",
            "Tag": ""
        }
    }
}
```

