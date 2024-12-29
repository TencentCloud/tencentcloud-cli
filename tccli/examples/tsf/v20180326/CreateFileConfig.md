**Example 1: 创建文件配置项**



Input: 

```
tccli tsf CreateFileConfig --cli-unfold-argument  \
    --ConfigName config_app \
    --ConfigVersion v1 \
    --ConfigVersionDesc This is desc \
    --ConfigFileName conf.txt \
    --ConfigFileValue config=enabled \
    --ConfigFileCode utf-8 \
    --ApplicationId application-5yr26r9a \
    --ConfigFilePath /root \
    --ConfigPostCmd sh start.sh \
    --EncodeWithBase64 True \
    --ProgramIdList program-6a79x94v
```

Output: 
```
{
    "Response": {
        "RequestId": "880b83c3-1018-4922-ab11-1822d5d5981d",
        "Result": true
    }
}
```

