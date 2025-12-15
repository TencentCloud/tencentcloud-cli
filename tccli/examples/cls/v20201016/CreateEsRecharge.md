**Example 1: 创建es导入任务**



Input: 

```
tccli cls CreateEsRecharge --cli-unfold-argument  \
    --Name template_1 \
    --TopicId 0335dd94-e327-435c-938c-d9d7a4525d45 \
    --Query  \
    --Index 65cdbbea-a06e-4e3b-a7a8-d8b365240f62_search \
    --ImportInfo.Type 2 \
    --ImportInfo.StartTime 1763367159 \
    --ImportInfo.MaxDelay 600 \
    --ImportInfo.CheckInterval 60 \
    --TimeInfo.Type 2 \
    --TimeInfo.TimeKey @timestamp \
    --TimeInfo.TimeFormat %Y-%m-%d %H:%M:%S.%f \
    --TimeInfo.TimeZone UTC+08:00 \
    --EsInfo.EsType 2 \
    --EsInfo.AccessMode 1 \
    --EsInfo.User elastic \
    --EsInfo.Password abc@***0 \
    --EsInfo.Address 127.0.0.1 \
    --EsInfo.Port 9200 \
    --EsInfo.VpcId vpc-***k \
    --EsInfo.VirtualGatewayType 1025
```

Output: 
```
{
    "Response": {
        "TaskId": "fc9170c0-95b9-4553-8f2d-32b12bf9d4d7",
        "RequestId": "609a4b29-4e49-4f34-bbca-b01a1e04f0b5"
    }
}
```

