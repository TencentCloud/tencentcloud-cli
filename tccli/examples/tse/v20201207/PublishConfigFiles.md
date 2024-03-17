**Example 1: 发布配置文件**

发布配置文件

Input: 

```
tccli tse PublishConfigFiles --cli-unfold-argument  \
    --InstanceId ins-fd191a86 \
    --ConfigFileReleases.Name ConfigFileReleases test \
    --ConfigFileReleases.Namespace Polaris \
    --ConfigFileReleases.Group group-test-jayhjxu \
    --ConfigFileReleases.FileName config-file-test \
    --ConfigFileReleases.Content I want you to act as a linux terminal. I will type commands and you will reply with what the terminal should show. I want you to only reply with the terminal output inside one unique code block, and nothing else. do not write explanations. do not type commands unless I instruct you to do so.  \
    --ConfigFileReleases.Comment test for 1 \
    --ConfigFileReleases.Version 12
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "abc"
    }
}
```

