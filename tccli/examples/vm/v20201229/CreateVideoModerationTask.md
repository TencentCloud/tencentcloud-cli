**Example 1: 回调签名示例**

当用户在创建审核任务时配置了Seed，我们则会在回调当时候加入签名参数，以保证数据的安全性。
签名方法：返回的HTTP头部，添加 `X-Signature` 的字段，值为： `seed ` +  `body ` 的 sha256 编码和Hex字符串。

例如：
假设用户 CallbackUrl 是：http://example.com, Seed 是： `dedb6dcc1cb7c63fde8fa5abfd57`，我们返回的回调的数据是： 
```{"TaskId": "task-video-X0zpcRUMzVidxj20","DataId":"test","Suggestion": "Block"}```,
则，审核完成后，我们会在调用 http://example.com 的时候，在HTTP 头部 传入`X-Signature` 的值为：
`74f0ae6d1f1e4eb1ffe4162da480a812f8a4dc19fe5a52bacbcd2c862d3edcfd`

> 备注： 回调Body格式请参考查询任务详情接口，回调Body格式和查询任务详情接口一致。

Input: 

```
tccli vm CreateVideoModerationTask --cli-unfold-argument  \
    --Type VIDEO \
    --CallbackUrl https://apis.example.com/callback/video \
    --Seed dedb6dcc1cb7c63fde8fa5abfd57 \
    --Tasks.0.DataId test \
    --Tasks.0.Input.Url https://test.myqcloud.com/test.mp4
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "DataId": "test",
                "TaskId": "c933aca1-90d2-4ab8-b045-f1b08069d76f",
                "Code": "OK",
                "Message": "Success"
            }
        ],
        "RequestId": "c933aca1-90d2-4ab8-b045-f1b08069d76f"
    }
}
```

**Example 2: 创建视频审核任务**

创建视频审核任务

Input: 

```
tccli vm CreateVideoModerationTask --cli-unfold-argument  \
    --Type VIDEO \
    --Tasks.0.DataId 0a782332-c9db-4cf5-a66e-20d60b4ea469 \
    --Tasks.0.Input.Url https://test.myqcloud.com/test.mp4
```

Output: 
```
{
    "Response": {
        "Results": [
            {
                "DataId": "0a782332-c9db-4cf5-a66e-20d60b4ea469",
                "TaskId": "c933aca1-90d2-4ab8-b045-f1b08069d76f",
                "Code": "OK",
                "Message": "Success"
            }
        ],
        "RequestId": "c933aca1-90d2-4ab8-b045-f1b08069d76f"
    }
}
```

