**Example 1: 查询容器镜像信息**

查询指定镜像仓库内全部容器镜像信息，获取镜像版本列表

Input: 

```
tccli tcr DescribeImages --cli-unfold-argument  \
    --RegistryId tcr-okmj78\
    --NamespaceName team-01\
    --RepositoryName nginx\
    --Limit 20\
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "3fdc859a-00fb-4ae4-a989-42eb387c6683",
        "ImageInfoList": [
            {
                "Digest": "sha256:ca30d8e9449eae19367f542aeb6e39764e94e7c34fca4277b9b7c77ba93eaa6c",
                "ImageVersion": "2.0",
                "Size": 63923200,
                "UpdateTime": "2020-02-14T06:45:40.40753972Z"
            },
            {
                "Digest": "sha256:0925d086715714114c1988f7c947db94064fd385e171a63c07730f1fa014e6f9",
                "ImageVersion": "1.0",
                "Size": 26733036,
                "UpdateTime": "2020-02-14T06:45:40.40753972Z"
            }
        ],
        "TotalCount": 2
    }
}
```

