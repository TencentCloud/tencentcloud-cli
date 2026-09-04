**Example 1: 列出指定推理服务绑定的 API Key**



Input: 

```
tccli dlc ListServiceApiKeys --cli-unfold-argument  \
    --ServiceId svc-20260615150835-n7pq \
    --StartTime 1781507306105 \
    --EndTime 1781507396105 \
    --Page 1 \
    --PageSize 200
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ApiKey": "sk-proj-Q4nRCLNS61ab3zoYyfVTX9bdotCV27SSdQMHe6dCz0yo5Zaf",
                "ApiKeyId": "apikey-20260615150836-trum",
                "AppId": 260200066,
                "CreateTime": 1781507316105,
                "Name": "xgboost-self-scale-test-key-20260615150836-ocbz",
                "ServiceId": "svc-20260615150835-n7pq",
                "ServiceName": "xgboost-self-scale-test",
                "Status": "Active",
                "SubAccountUin": "700002655694",
                "Uin": "700002655694",
                "UpdateTime": 1781507316105
            }
        ],
        "Page": 1,
        "PageSize": 200,
        "Total": 1,
        "TotalPages": 1,
        "RequestId": "f95d41eb-5d67-4dde-a579-d46af86d1ca5"
    }
}
```

