**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveCallbackTemplate --cli-unfold-argument  \
    --TemplateId 1000
```

Output: 
```
{
    "Response": {
        "Template": {
            "TemplateId": 1000,
            "TemplateName": "testName",
            "Description": "test",
            "StreamBeginNotifyUrl": "http://www.qq.com/api/notify?action=streamBegin",
            "StreamEndNotifyUrl": "http://www.qq.com/api/notify?action=streamEnd",
            "StreamMixNotifyUrl": "",
            "RecordNotifyUrl": "http://www.qq.com/api/notify?action=record",
            "SnapshotNotifyUrl": "http://www.qq.com/api/notify?action=record",
            "PornCensorshipNotifyUrl": "http://www.qq.com/api/notify?action=porn",
            "CallbackKey": "adasdasda1312312"
        },
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

