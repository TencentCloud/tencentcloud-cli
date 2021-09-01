**Example 1: 请求示例**



Input: 

```
tccli live ModifyLiveCallbackTemplate --cli-unfold-argument  \
    --TemplateId 1000 \
    --TemplateName testName \
    --Description test \
    --CallbackKey adasdas23432423 \
    --StreamBeginNotifyUrl http://www.yourdomain.com/api/notify?action \
    --StreamEndNotifyUrl http://www.yourdomain.com/api/notify?action \
    --RecordNotifyUrl http://www.yourdomain.com/api/notify?action \
    --SnapshotNotifyUrl http://www.yourdomain.com/api/notify?action \
    --PornCensorshipNotifyUrl http://www.yourdomain.com/api/notify?action
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

