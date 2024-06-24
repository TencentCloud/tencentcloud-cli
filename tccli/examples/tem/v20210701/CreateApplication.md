**Example 1: 创建应用**

创建应用

Input: 

```
tccli tem CreateApplication --cli-unfold-argument  \
    --ApplicationName abc \
    --Description abc \
    --UseDefaultImageService 0 \
    --RepoType 0 \
    --InstanceId abc \
    --RepoServer abc \
    --RepoName abc \
    --SourceChannel 0 \
    --SubnetList abc \
    --CodingLanguage abc \
    --DeployMode abc \
    --EnableTracing 0 \
    --UseDefaultImageServiceParameters.EnterpriseInstanceName abc \
    --UseDefaultImageServiceParameters.EnterpriseInstanceChargeType 0 \
    --UseDefaultImageServiceParameters.EnterpriseInstanceType abc \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc
```

Output: 
```
{
    "Response": {
        "Result": "abc",
        "RequestId": "abc"
    }
}
```

