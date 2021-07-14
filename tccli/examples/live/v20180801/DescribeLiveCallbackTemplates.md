**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveCallbackTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Templates": [
            {
                "TemplateId": 1000,
                "TemplateName": "testName",
                "Description": "test",
                "StreamBeginNotifyUrl": "http://www.qq.com/api/notify?action=streamBegin",
                "StreamEndNotifyUrl": "http://www.qq.com/api/notify?action=streamEnd",
                "StreamMixNotifyUrl": "",
                "RecordNotifyUrl": "http://www.qq.com/api/notify?action=record",
                "SnapshotNotifyUrl": "http://www.qq.com/api/notify?action=record",
                "PornCensorshipNotifyUrl": "http://www.qq.com/api/notify?action=porn",
                "CallbackKey": "adafas1412423432"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

