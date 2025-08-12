**Example 1: 创建es导入任务**



Input: 

```
tccli cls CreateEsRecharge --cli-unfold-argument  \
    --TopicId 0335dd94-e327-435c-938c-d9d7a4525d45 \
    --Name es_test \
    --Index 65cdbbea-a06e-4e3b-a7a8-d8b365240f62_search \
    --Query  \
    --EsInfo.EsType 2 \
    --EsInfo.AccessMode 2 \
    --EsInfo.User es_user \
    --EsInfo.Address 127.0.0.1 \
    --EsInfo.Port 9200 \
    --EsInfo.Password abc@syz \
    --ImportInfo.Type 1 \
    --TimeInfo.Type 1
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

