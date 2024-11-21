**Example 1: 查询Chart包下载信息**



Input: 

```
tccli tcr DescribeChartDownloadInfo --cli-unfold-argument  \
    --RegistryId tcr-test123 \
    --NamespaceName mytest \
    --ChartName mytest \
    --ChartVersion 1.0
```

Output: 
```
{
    "Response": {
        "PreSignedDownloadURL": "http://tcr-mfoeec7x-1251707795.cos.ap-beijing.myqcloud.com/mytest%2Faaa-1.0.tgz?x-cos-security-token=************************************************************",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

