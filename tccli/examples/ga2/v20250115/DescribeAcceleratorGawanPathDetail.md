**Example 1: 查询GAWAN路径详情**



Input: 

```
tccli ga2 DescribeAcceleratorGawanPathDetail --cli-unfold-argument  \
    --GlobalAcceleratorId ga-h1dwqipu
```

Output: 
```
{
    "Response": {
        "AcceleratorGawanPathDetail": [
            {
                "GawanPathList": [
                    {
                        "DstRegion": "ap-singapore",
                        "ForwardPathSet": {
                            "PathList": [
                                {
                                    "CrossBorderType": 3,
                                    "EdgeList": [
                                        {
                                            "EdgeId": "edge-jda1je5i",
                                            "EdgeType": 1,
                                            "LocalCloudType": "TENCENT",
                                            "LocalClusterId": "gapclu-2e223p0f",
                                            "LocalClusterName": "ap-beijing_site-1",
                                            "LocalGawanIpList": [
                                                {
                                                    "ForwardIp": "10.102.8.38",
                                                    "HostIp": "10.102.0.7",
                                                    "InstanceId": "ins-p4psqa1v",
                                                    "PublicIp": ""
                                                }
                                            ],
                                            "LocalRegion": "ap-beijing",
                                            "RemoteCloudType": "TENCENT",
                                            "RemoteClusterId": "gapclu-hfepqq35",
                                            "RemoteClusterName": "ap-guangzhou_site-1-wins",
                                            "RemoteGawanIpList": [
                                                {
                                                    "ForwardIp": "10.101.8.4",
                                                    "HostIp": "10.101.0.12",
                                                    "InstanceId": "ins-bzg9oh52",
                                                    "PublicIp": ""
                                                }
                                            ],
                                            "RemoteRegion": "ap-guangzhou"
                                        }
                                    ],
                                    "PathId": "path-9twtq0md",
                                    "PlaneId": 3,
                                    "PlaneType": 2
                                }
                            ],
                            "PathSetId": "paths-5xosqpau"
                        },
                        "ReversePathSet": {
                            "PathList": [
                                {
                                    "CrossBorderType": 3,
                                    "EdgeList": [
                                        {
                                            "EdgeId": "edge-efio32x4",
                                            "EdgeType": 2,
                                            "LocalCloudType": "TENCENT",
                                            "LocalClusterId": "gapclu-k1kloo7r",
                                            "LocalClusterName": "ap-singapore_site-2",
                                            "LocalGawanIpList": [
                                                {
                                                    "ForwardIp": "10.106.40.14",
                                                    "HostIp": "10.106.32.10",
                                                    "InstanceId": "ins-8p1ff6wy",
                                                    "PublicIp": ""
                                                }
                                            ],
                                            "LocalRegion": "ap-singapore",
                                            "RemoteCloudType": "TENCENT",
                                            "RemoteClusterId": "gapclu-qe1c9mez",
                                            "RemoteClusterName": "ap-hongkong_site-2",
                                            "RemoteGawanIpList": [
                                                {
                                                    "ForwardIp": "10.105.8.4",
                                                    "HostIp": "10.105.0.10",
                                                    "InstanceId": "ins-9g61m75y",
                                                    "PublicIp": ""
                                                }
                                            ],
                                            "RemoteRegion": "ap-hongkong"
                                        }
                                    ],
                                    "PathId": "path-cl84z4o9",
                                    "PlaneId": 3,
                                    "PlaneType": 2
                                }
                            ],
                            "PathSetId": "paths-hp5qhl0c"
                        },
                        "SrcRegion": "ap-beijing"
                    }
                ],
                "GlobalAcceleratorId": "ga-h1dwqipu"
            }
        ],
        "RequestId": "94e45435-2083-4559-9ee8-4f4539e3fea1"
    }
}
```

