**Example 1: 接口调用成功示例**

上传高级运行参数-成功

Input: 

```
tccli wedata GetAdvanceRunParams --cli-unfold-argument  \
    --ProjectId 822739339334606848 \
    --AdvanceRunParam aa \
    --RemotePath /datastudio/project/822739339334606848/默认文件夹/dd.sql \
    --OriginalParams abc
```

Output: 
```
{
    "Response": {
        "RequestId": "123",
        "Result": "true",
        "Data": "aaa"
    }
}
```

**Example 2: 请求失败示例**

上传高级运行参数-失败

Input: 

```
tccli wedata GetAdvanceRunParams --cli-unfold-argument  \
    --ProjectId 822739339334606848 \
    --RemotePath /datastudio/project/822739339334606848/默认文件夹/dd.sql \
    --AdvanceRunParam aa \
    --OriginalParams abc
```

Output: 
```
{
    "Response": {
        "RequestId": "b7cc8a2d-60c5-461f-b35f-74a3a6b2259d",
        "Result": false,
        "Data": ""
    }
}
```

