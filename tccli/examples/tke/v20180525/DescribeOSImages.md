**Example 1: 获取镜像聚合信息**



Input: 

```
tccli tke DescribeOSImages --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "OSImageSeriesSet": [
            {
                "Alias": "CentOS 7.2 64bit",
                "ImageId": "img-rkiynh11",
                "OsCustomizeType": "GENERAL",
                "OsName": "centos7.2x86_64",
                "SeriesName": "centos7.2x86_64",
                "Status": "online"
            }
        ],
        "RequestId": "899c6fe7-f87d-4232-b1a8-82b81acfa037",
        "TotalCount": 11
    }
}
```

