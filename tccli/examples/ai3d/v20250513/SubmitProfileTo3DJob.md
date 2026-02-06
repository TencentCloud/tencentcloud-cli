**Example 1: 成功调用**

成功提交任务

Input: 

```
tccli ai3d SubmitProfileTo3DJob --cli-unfold-argument  \
    --Profile.Url https://***.cos.ap-guangzhou.myqcloud.com/***.jpg \
    --Template basketball
```

Output: 
```
{
    "Response": {
        "JobId": "1321332059964817408",
        "RequestId": "177604c6-3647-4b7a-a637-cb00a24cf215"
    }
}
```

