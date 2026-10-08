**Example 1: 任务不存在**



Input: 

```
tccli mps QueryHunyuan3DTask --cli-unfold-argument  \
    --TaskId 4deda860-a9a0-47e3-81f1-00cadf02a44c
```

Output: 
```
{
    "Response": {
        "ErrorCode": "ResourceNotFound.TaskId",
        "ErrorMessage": "task not found or expired",
        "RequestId": "cec25a1e-0875-44f0-87da-2a1ebabee48b"
    }
}
```

**Example 2: 回包较为完整的示例**



Input: 

```
tccli mps QueryHunyuan3DTask --cli-unfold-argument  \
    --TaskId r_75466f84b0b911f1b1b66aacb78dd458
```

Output: 
```
{
    "Response": {
        "CreateTime": "2026-09-15T03:56:40Z",
        "FaceCount": 500000,
        "Progress": 100,
        "Prompt": "a cute chicken, cartoon style",
        "ResultFile3Ds": [
            {
                "PreviewImageUrl": "https://hunyuan-base-prod-1258344703.cos.ap-guangzhou.myqcloud.com/openapi/text2img/838676194d9cada36394b6ef08ee9bac.png?q-ak=************************************&q-header-list=&q-key-time=1789444785%3B1789531185&q-sign-algorithm=sha1&q-sign-time=1789444785%3B1789531185&q-signature=1559acdb874c9459b83599b5b6cae25f13f0dabd&q-url-param-list=",
                "Type": "GLB",
                "Url": "https://hunyuan-3d-1258344703.cos.ap-guangzhou.myqcloud.com/gen_tmp_test/efcec080d3e049c3911d5781518e59e7/946764dab065116e55f6204f00e43eab.glb?q-sign-algorithm=sha1&q-ak=************************************&q-sign-time=1789444780%3B1789531180&q-key-time=1789444780%3B1789531180&q-header-list=&q-url-param-list=&q-signature=cbc0494a4e5504a41d53698f2916ca8845a3e9f9"
            }
        ],
        "Status": "DONE",
        "TaskId": "r_75466f84b0b911f1b1b66aacb78dd458",
        "TaskType": "text_to_3d",
        "UpdateTime": "2026-09-15T04:00:14Z",
        "RequestId": "531aa6de-1144-4797-9b87-b8c79c998160"
    }
}
```

**Example 3: 返回RefImage**



Input: 

```
tccli mps QueryHunyuan3DTask --cli-unfold-argument  \
    --TaskId r_e6fb6e39b0ba11f1b1b66aacb78dd458
```

Output: 
```
{
    "Response": {
        "CreateTime": "2026-09-15T04:07:01Z",
        "FaceCount": 500000,
        "Progress": 0,
        "RefImage": "https://hunyuan-base-test-1258344703.cos.ap-guangzhou.myqcloud.com/public/test/eba3542f-5e19-4862-b95d-c2d28e7ef91e-latent.png",
        "Status": "RUN",
        "TaskId": "r_e6fb6e39b0ba11f1b1b66aacb78dd458",
        "TaskType": "image_to_3d",
        "UpdateTime": "2026-09-15T04:07:18Z",
        "RequestId": "7b545f16-7552-4cc9-acfc-04cdc60581e8"
    }
}
```

