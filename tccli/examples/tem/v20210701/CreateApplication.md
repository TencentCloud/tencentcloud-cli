**Example 1: 创建应用**

创建应用

Input: 

```
tccli tem CreateApplication --cli-unfold-argument  \
    --ApplicationName xx \
    --SubnetList xx \
    --Description xx \
    --InstanceId xx \
    --DeployMode xx \
    --RepoServer xx \
    --SourceChannel 0 \
    --RepoType 0 \
    --RepoName xx \
    --UseDefaultImageService 0 \
    --CodingLanguage xx
```

Output: 
```
{
    "Response": {
        "Result": "xx",
        "RequestId": "xx"
    }
}
```

