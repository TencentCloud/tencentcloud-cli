**Example 1: 查询知识库组件的版本列表**

查询ristretto组件的版本列表

Input: 

```
tccli bsca DescribeKBComponentVersionList --cli-unfold-argument  \
    --PURL.Name ristretto \
    --PURL.Protocol golang \
    --PURL.Namespace  \
    --PURL.Subpath  \
    --PURL.Version 
```

Output: 
```
{
    "Response": {
        "VersionList": [
            {
                "LicenseExpression": "gpl-3.0",
                "PURL": {
                    "Name": "xxl-job-core",
                    "Namespace": "com.xuxueli",
                    "Protocol": "maven",
                    "Qualifiers": [],
                    "Subpath": "",
                    "Version": "2.4.1"
                },
                "VersionInfo": {
                    "CopyrightList": [],
                    "PublishTime": "2024-04-17 08:50:11.000000",
                    "TagList": [
                        "ContainsVulnerability"
                    ]
                }
            }
        ],
        "RequestId": "101705d6-b972-4dbf-9d10-0b075d509d3d"
    }
}
```

