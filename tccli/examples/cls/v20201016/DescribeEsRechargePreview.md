**Example 1: es数据预览**



Input: 

```
tccli cls DescribeEsRechargePreview --cli-unfold-argument  \
    --Name preview_test \
    --TopicId d8f1bad5-80ad-427a-8dc9-3108778e39aa \
    --Index louder_search \
    --Query ab \
    --EsInfo.EsType 2 \
    --EsInfo.AccessMode 2 \
    --EsInfo.User es_user \
    --EsInfo.Address 127.0.0.1 \
    --EsInfo.Port 9200 \
    --EsInfo.Password abc@syz \
    --ImportInfo.Type 1 \
    --ImportInfo.MaxDelay 120 \
    --ImportInfo.CheckInterval 60 \
    --TimeInfo.Type 1
```

Output: 
```
{
    "Response": {
        "Data": [
            "{\"@__TIMESTAMP__\":1747258435179,\"Label_index\":null}"
        ],
        "RequestId": "e0897b10-09df-49de-b0ec-8644f12972ec"
    }
}
```

