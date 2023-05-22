**Example 1: 请求示例**

请求示例

Input: 

```
tccli live ModifyLiveCallbackTemplate --cli-unfold-argument  \
    --StreamBeginNotifyUrl http://www.yourdomain.com/api/notify?action=streamBegin \
    --StreamEndNotifyUrl http://www.yourdomain.com/api/notify?action=streamEnd \
    --TemplateName testName \
    --RecordNotifyUrl http://www.yourdomain.com/api/notify?action=record \
    --SnapshotNotifyUrl http://www.yourdomain.com/api/notify?action=snapshot \
    --TemplateId 1000 \
    --PornCensorshipNotifyUrl http://www.yourdomain.com/api/notify?action=porn \
    --CallbackKey adasdas23432423 \
    --Description test
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

