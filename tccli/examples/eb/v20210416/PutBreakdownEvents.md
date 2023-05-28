**Example 1: 故障事件上报demo**

发送事件

Input: 

```
tccli eb PutBreakdownEvents --cli-unfold-argument  \
    --EventList.0.SpecVersion 1.0 \
    --EventList.0.Id 22222 \
    --EventList.0.Source cvm.cloud.tencent \
    --EventList.0.Type cvm:breakdown:xxx \
    --EventList.0.AlarmTime 1683599998927 \
    --EventList.0.RecoverTime None \
    --EventList.0.Region ap-guangzhou \
    --EventList.0.Zone ap-guangzhou-1 \
    --EventList.0.Status 2 \
    --EventList.0.Data.Instances.0.InstanceId ins-xxx \
    --EventList.0.Data.Instances.0.AppId 123 \
    --EventList.0.Data.Instances.0.Uin 456 \
    --EventList.0.Data.Instances.0.Status 2 \
    --EventList.0.Data.Description test \
    --EventList.0.Data.InternalReason test \
    --EventList.0.Data.ExternalReason test \
    --EventList.0.Data.RecoverAdvise test \
    --EventList.0.Data.LocationTool test \
    --EventList.0.Data.Follower allenmzhang \
    --EventList.0.Data.Handler allenmzhang \
    --EventList.0.Data.Owner allenmzhang
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

