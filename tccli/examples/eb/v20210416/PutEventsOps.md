**Example 1: demo**

发送事件

Input: 

```
tccli eb PutEventsOps --cli-unfold-argument  \
    --EventList.0.Data {"Category":0,"Area":0,"Zone":"ap-guangzhou-1"} \
    --EventList.0.DataContentType application/json;charset=utf-8 \
    --EventList.0.Id b7ef8793-7bbc-449c-abf5-71f5b022ec60 \
    --EventList.0.Region ap-guangzhou \
    --EventList.0.Source cvm.cloud.tencent \
    --EventList.0.SpecVersion 1.0 \
    --EventList.0.Status 1 \
    --EventList.0.Subject all \
    --EventList.0.Time 1670847967164 \
    --EventList.0.Type cvm:statuspage:xxx
```

Output: 
```
{
    "Response": {
        "RequestId": "9178600d-67ba-4f25-9d6c-4f8ab3f32ccc",
        "EventList": [
            {
                "Id": "b7ef8793-7bbc-449c-abf5-71f5b022ec60"
            }
        ]
    }
}
```

