**Example 1: 计量商品用量提醒**



Input: 

```
tccli market FlowProductRemind --cli-unfold-argument  \
    --LeftFlow 200 \
    --ResourceId market-g9sjptwqi \
    --FlowUnit Mb \
    --TotalFlow 2000 \
    --ProviderUin 12345678 \
    --SignId 1054492229
```

Output: 
```
{
    "Response": {
        "Info": "",
        "FlowId": "7c0b5ac4-47a6-448b-b486-18d9774e3264",
        "RequestId": "1f219bf9-8037-48ab-ace4-4b14b6a42146",
        "Success": "true"
    }
}
```

