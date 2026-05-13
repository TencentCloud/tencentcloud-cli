**Example 1: 修改服务角色自定义镜像**

修改服务角色自定义镜像

Input: 

```
tccli emr ModifyComponentImage --cli-unfold-argument  \
    --InstanceId emr-2rbbuac8 \
    --ServiceGroup 6 \
    --ServiceType 17 \
    --CustomImage.ImageSourceType tcr \
    --CustomImage.ImageInfo.RegistryId tcr-qickpmsq \
    --CustomImage.ImageInfo.DomainName tcr-test.tencentcloudcr.com \
    --CustomImage.ImageInfo.NamespaceName default \
    --CustomImage.ImageInfo.RepositoryName spark \
    --CustomImage.ImageInfo.ImageVersion v3.3.2 \
    --CustomImage.ImageInfo.ImagePullPolicy Always \
    --CustomImage.ImageInfo.Image tcr-test.tencentcloudcr.com/test/spark:v3.3.2 \
    --CustomImage.ImagePullSecret.SourceNamespace emr \
    --CustomImage.ImagePullSecret.SecretNames name_test \
    --Rebuild False
```

Output: 
```
{
    "Response": {
        "RequestId": "326c14b9-6371-4767-8ab6-8f2f6ba71396",
        "FlowId": 0
    }
}
```

