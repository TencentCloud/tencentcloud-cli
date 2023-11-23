**Example 1: 创建版本部署任务**

将站点 ID 为 zone-32qwgrnvbisw 下版本 ID 为 ver-2ogs1as803hm 的版本发布到环境 ID 为 env-28jw51ksm9bw 的环境中。

Input: 

```
tccli teo DeployConfigGroupVersion --cli-unfold-argument  \
    --ZoneId zone-32qwgrnvbisw \
    --EnvId env-28jw51ksm9bw \
    --ConfigGroupVersionInfos.0.VersionId ver-2ogs1as803hm \
    --Description Add IPv6 and AccelerationMainland configuration
```

Output: 
```
{
    "Response": {
        "RequestId": "5e0a2b4e-df6d-4d2a-as19-1706cbf8a902",
        "RecordId": "dr-2nvadq3sa41u"
    }
}
```

