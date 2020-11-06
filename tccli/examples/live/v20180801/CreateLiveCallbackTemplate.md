**Example 1: Sample request**



Input: 

```
tccli live CreateLiveCallbackTemplate --cli-unfold-argument  \
    --TemplateName testName \
    --Description test \
    --CallbackKey adasda131312 \
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
        "TemplateId": 1000,
        "RequestID": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

