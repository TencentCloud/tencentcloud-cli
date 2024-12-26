**Example 1: 请求示例**

当需要查询一个导播台的信息时，可以按如下调用。

Input: 

```
tccli live DescribeCaster --cli-unfold-argument  \
    --CasterId 63501
```

Output: 
```
{
    "Response": {
        "CasterInfo": {
            "CasterId": 63501,
            "CasterName": "example",
            "StartLiveTime": 0,
            "Description": "",
            "CreateTime": 1603158528,
            "Status": 0,
            "ExpireTime": -1,
            "DelayTime": 0,
            "PgmWidth": 0,
            "PgmHeight": 0,
            "PgmFps": 0,
            "PgmBitRate": 0,
            "PgmAudioBitRate": 256,
            "FeeType": 0,
            "RecordTemplateId": 0,
            "RecordStatus": 0,
            "RecordTaskId": ""
        },
        "RequestId": "bebdd4e4-4087-411b-ab2e-3692dcfba4c3"
    }
}
```

