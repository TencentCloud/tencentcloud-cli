**Example 1: 安装模型调用示例**



Input: 

```
tccli es InstallInstanceModel --cli-unfold-argument  \
    --InstanceId es-xxxxxxxx \
    --UsrCosModelUrlList https://modeltestxxxx-sh-12560502xx.cos.ap-shanghai.myqcloud.com/bge-base-zh-v1.5.zip \
    --ModelNames wit-test \
    --TaskTypes text_embedding
```

Output: 
```
{
    "Response": {
        "RequestId": "d6c1d15f-5eab-11ef-9b1d-525400a23f29",
        "FlowId": "17279"
    }
}
```

