**Example 1: 创建文件配置项**



Input: 

```
tccli tsf CreateFileConfig --cli-unfold-argument  \
    --ApplicationId application-dapbkdgy \
    --ConfigName war-config \
    --ConfigVersion 1 \
    --ConfigFileName update \
    --ConfigFileCode utf-8 \
    --ConfigPostCmd /usr/bin/bash \
    --ConfigFileValue workdir \
    --ConfigFilePath /root
```

Output: 
```
{
    "Response": {
        "RequestId": "3063d6c8-9801-4ed0-b306-be14b89f6133",
        "Result": true
    }
}
```

