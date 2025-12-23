**Example 1: 调用成功示例**



Input: 

```
tccli aiart DescribeTemplateToImageJob --cli-unfold-argument  \
    --JobId 1394637692053602304
```

Output: 
```
{
    "Response": {
        "ErrorCode": "",
        "ErrorMessage": "",
        "ResultImage": [
            "https://***.tencentcos.cn/imagestyle/results/***/b1759140-6951-4d6a-9f12-add42ca16b***ey-time=1766401936%3B1766488336&q-header-list=host&q-url-param-list=&q-signature=dfea613edc2ee44c44ee1c4be393ea355cfa5487"
        ],
        "Status": "DONE",
        "RequestId": "1378c58c-f636-42c2-a5fd-814d3c24e594"
    }
}
```

