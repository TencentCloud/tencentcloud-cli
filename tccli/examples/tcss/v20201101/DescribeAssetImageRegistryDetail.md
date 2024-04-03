**Example 1: 查看仓库镜像详情**



Input: 

```
tccli tcss DescribeAssetImageRegistryDetail --cli-unfold-argument  \
    --Id 5427
```

Output: 
```
{
    "Response": {
        "RequestId": "acc92f01-ee14-4eec-a1b6-e78d3ea0b7e9",
        "ImageDigest": "sha256:615475135bb705517e749767a28f6bd57199008d3e9b688efa0f73a8befccc97",
        "ImageId": "sha256:e68ba1280908f76a9e22a813b9ea0c7358e9bcf0ed616fddf88dad557e33d1ca",
        "RegistryType": "ccr",
        "ImageRepoAddress": "ccr.ccs.tencentyun.com/yunding/person1",
        "InstanceId": "",
        "InstanceName": "ccr-default",
        "Namespace": "yunding",
        "ImageName": "person1",
        "ImageTag": "v1",
        "ImageSize": 74866818,
        "ScanTime": "2022-01-14T21:03:19+08:00",
        "ScanStatus": "SCANNED",
        "Progress": 100,
        "VulCnt": 172,
        "VirusCnt": 0,
        "RiskCnt": 1,
        "SentiveInfoCnt": 1,
        "OsName": "linux",
        "ScanVirusError": "",
        "ScanVulError": "",
        "ScanRiskError": "",
        "ScanVirusProgress": 0,
        "ScanVulProgress": 100,
        "ScanRiskProgress": 100,
        "ScanRemainTime": 0,
        "CveStatus": "SCANNED",
        "RiskStatus": "SCANNED",
        "VirusStatus": "NOT_SCAN",
        "IsAuthorized": 1,
        "LayerInfo": "#2020-06-17 00:22:24.918233762 +0000 UTC\n\n/bin/sh -c #(nop) ADD file:84700c11fcc969ac08ef25f115513d76c7b72a4118c01fbc86ef0a6056fdebeb in / \n\n#2020-06-17 00:22:25.276021438 +0000 UTC\n\n/bin/sh -c #(nop)  LABEL org.label-schema.schema-version=1.0 org.label-schema.name=CentOS Base Image org.label-schema.vendor=CentOS org.label-schema.license=GPLv2 org.label-schema.build-date=20200611\n\n#2020-06-17 00:22:25.47282687 +0000 UTC\n\n/bin/sh -c #(nop)  CMD [\"/bin/bash\"]\n\n#2020-12-18 10:06:01.1576746 +0000 UTC\n\n/bin/sh -c echo \"RSYNC_PASSWORD='xxx' rsync\"\n\n",
        "RegistryRegion": "default",
        "ImageCreateTime": "2020-12-25T16:40:39+08:00"
    }
}
```

**Example 2: 镜像仓库查询镜像仓库详情**



Input: 

```
tccli tcss DescribeAssetImageRegistryDetail --cli-unfold-argument  \
    --Id 3421599
```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "ImageDigest": "sha256:8d8faaa36c253a8745c392fc71640757d29a5f026fc0e44bb9c98d56544f5175",
        "ImageId": "sha256:bb804a9c85d7199b8fd6a0c1a34ef1d049689604046fc5ce1ee6b968de78281b",
        "RegistryType": "ccr",
        "ImageRepoAddress": "hkccr.ccs.tencentyun.com/mhzou/mhccrxg",
        "InstanceId": "",
        "InstanceName": "ccr-ap-hongkong",
        "Namespace": "mhzou",
        "ImageName": "mhccrxg",
        "ImageTag": "mhccrxg1",
        "ImageSize": 8544764,
        "ScanTime": "2022-01-19T22:58:23+08:00",
        "ScanStatus": "SCANNED",
        "Progress": 100,
        "VulCnt": 2425,
        "VirusCnt": 0,
        "RiskCnt": 0,
        "SentiveInfoCnt": 0,
        "OsName": "linux",
        "ScanVirusError": "",
        "ScanVulError": "",
        "ScanRiskError": "",
        "ScanVirusProgress": 0,
        "ScanVulProgress": 100,
        "ScanRiskProgress": 100,
        "ScanRemainTime": 0,
        "CveStatus": "SCANNED",
        "RiskStatus": "SCANNED",
        "VirusStatus": "NOT_SCAN",
        "IsAuthorized": 1,
        "LayerInfo": "xxx",
        "RegistryRegion": "ap-hongkong",
        "ImageCreateTime": "1900-01-01T00:00:00+00:00"
    }
}
```

