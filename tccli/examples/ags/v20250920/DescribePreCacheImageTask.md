**Example 1: 查询预热任务状态**



Input: 

```
tccli ags DescribePreCacheImageTask --cli-unfold-argument  \
    --Image test.tencentcloudcr.com/example/app:0.2.2 \
    --ImageDigest sha256:39e2c18395c3105fce919dasdqwe85cd775d380e83581b132d8d742761123a1e675 \
    --ImageRegistryType enterprise
```

Output: 
```
{
    "Response": {
        "Image": "test.tencentcloudcr.com/example/app:0.2.2",
        "ImageDigest": "sha256:39e2c18395c3105fce919dasdqwe85cd775d380e83581b132d8d742761123a1e675",
        "ImageRegistryType": "enterprise",
        "Message": "........",
        "RequestId": "a34158c5-d383-49ae-9b36-d37da3fde06f",
        "Status": "Success"
    }
}
```

