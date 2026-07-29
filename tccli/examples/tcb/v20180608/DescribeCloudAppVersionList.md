**Example 1: 查询云应用服务版本列表**



Input: 

```
tccli tcb DescribeCloudAppVersionList --cli-unfold-argument  \
    --EnvId env-xx12 \
    --DeployType static-hosting \
    --ServiceName vue \
    --PageSize 10 \
    --PageNo 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "VersionList": [
            {
                "BuildId": "2600520664",
                "BuildTime": "2026-03-12 17:08:31",
                "BuildType": "TEMPLATE",
                "Framework": "react",
                "StaticConfig": {
                    "AppPath": "/React",
                    "BuildPath": "./dist",
                    "CodeBranch": "main",
                    "CodeRepo": "cloudrun",
                    "CodeSource": "github",
                    "CosSuffix": "cos-xx",
                    "CosTimestamp": "1600520664",
                    "Framework": "react",
                    "NodeJsVersion": "20",
                    "StaticCmd": {
                        "BuildCmd": "npm run build",
                        "DeployCmd": "tcb hosting deploy ./dist /React",
                        "InstallCmd": "npm install"
                    },
                    "StaticEnv": {
                        "Variables": [
                            {
                                "Key": "VITE_ENV_ID",
                                "Value": "env-xx12"
                            }
                        ]
                    },
                    "ZipFileUrl": "https://example.com/weda-uploader/5*b*8*********0e02af98894fa96b28-raact-template.zip"
                },
                "Status": "SUCCESS",
                "VersionName": "React-test-001"
            }
        ],
        "RequestId": "d1aa2bbe-b1d5-498f-9b2e-9f74d0315907"
    }
}
```

**Example 2: 查询自定义云应用列表**



Input: 

```
tccli tcb DescribeCloudAppVersionList --cli-unfold-argument  \
    --EnvId lowcode-*********98f7294 \
    --DeployType custom \
    --ServiceName my-docker-build-v1 \
    --PageSize 1 \
    --PageNo 1
```

Output: 
```
{
    "Response": {
        "Total": 17,
        "VersionList": [
            {
                "BuildId": "2600928843",
                "BuildTime": "2026-05-18 17:43:14",
                "BuildType": "v2",
                "Framework": "",
                "StaticConfig": {
                    "AppPath": "",
                    "BuildPath": "",
                    "CodeBranch": "",
                    "CodeRepo": "",
                    "CodeSource": "",
                    "CosSuffix": "",
                    "CosTimestamp": "",
                    "Framework": "",
                    "NodeJsVersion": "",
                    "StaticCmd": {
                        "BuildCmd": "",
                        "DeployCmd": "",
                        "InstallCmd": ""
                    },
                    "StaticEnv": {
                        "Variables": null
                    },
                    "ZipFileUrl": ""
                },
                "Status": "FAILED",
                "Steps": [
                    {
                        "Duration": "493ms",
                        "Name": "检出 ZIP 包",
                        "Status": "success"
                    }
                ],
                "VersionName": "my-docker-build-v1-017"
            }
        ],
        "RequestId": "92900e53-2ff1-4338-9a45-041008db13cb"
    }
}
```

