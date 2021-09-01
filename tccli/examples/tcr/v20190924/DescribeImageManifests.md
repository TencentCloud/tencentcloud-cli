**Example 1: 查询容器镜像Manifest信息**



Input: 

```
tccli tcr DescribeImageManifests --cli-unfold-argument  \
    --RegistryId tcr-7s2d14fn \
    --NamespaceName test \
    --RepositoryName mytest \
    --ImageVersion 1.0
```

Output: 
```
{
    "Response": {
        "RequestId": "6ef83620-c92e-496c-b206-25b0b638f409",
        "Manifest": "{\"config\":{\"digest\":\"sha256:72f6114b119f1423a2713aca1e15cb9aeadf835a714d36f7a2cf88d10e4bb6be\",\"mediaType\":\"application/vnd.docker.container.image.v1+json\",\"size\":2396},\"layers\":[{\"digest\":\"sha256:9123ac7c32f74759e6283f04dbf571f18246abe5bb2c779efcb32cd50f3ff13c\",\"mediaType\":\"application/vnd.docker.image.rootfs.diff.tar.gzip\",\"size\":2764173},{\"digest\":\"sha256:8673ef3ff8fc5ede7363cbe74d295b013ef7959ba002af607314d8ee77b58a5a\",\"mediaType\":\"application/vnd.docker.image.rootfs.diff.tar.gzip\",\"size\":1616975},{\"digest\":\"sha256:a8e22d4a83517ee59537183a2f7ca35fa7b81d36176a9d5d42ca2ab0486af779\",\"mediaType\":\"application/vnd.docker.image.rootfs.diff.tar.gzip\",\"size\":8446306}],\"mediaType\":\"application/vnd.docker.distribution.manifest.v2+json\",\"schemaVersion\":2}",
        "Config": ""
    }
}
```

