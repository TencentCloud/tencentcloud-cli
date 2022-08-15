**Example 1: 查询容器镜像信息**

查询指定镜像仓库内全部容器镜像信息，获取镜像版本列表

Input: 

```
tccli tcr DescribeImages --cli-unfold-argument  \
    --Limit 20 \
    --NamespaceName team-01 \
    --RepositoryName nginx \
    --RegistryId tcr-okmj78 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "d76f7a1b-d9e9-4454-b95b-25c34f17b943",
        "ImageInfoList": [
            {
                "Digest": "sha256:a1801b843b1bfaf77c501e7a6d3f709401a1e0c83863037fa3aab063a7fdb9dc",
                "ImageVersion": "8",
                "Size": 83520757,
                "UpdateTime": "2022-08-06T07:31:01.207374Z",
                "Kind": "Artifact::application/vnd.docker.distribution.manifest.v2+json",
                "KmsSignature": "UKauWpHdjaTjTsE64BSFhJe0YZj7eXiu8DzkRgTk0vbuxl+ICYbVJ2p1afHGv/WsOqqJvEKJdNPU4iAGNYEbegTi/UwcrCRijNeFkzHNqljBa75g1u9LHjVmtE9dxzh17YGRHpDxbL2CCjZ9YgeCqppsl1LiXvlYdrMLgoqwHKwao3WnkZU2fye4HIreZ3CXGkjv7g8rbhmjwEZJUTWAuEws7eNSvl9RS8NAJctwvZWZQUGKkRpbBRkKxdENSIgRoA+SyX0Qmu2SxvwDRTsCwI+B1rJxLmw1wYgAh3mQiXtehBZAJdYLcOvokUgAUC8cpKpeJ+bSsYvCLh+uJlF4Pg=="
            }
        ],
        "TotalCount": 1
    }
}
```

