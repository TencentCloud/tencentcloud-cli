**Example 1: 列出 API Key（全量分页）**



Input: 

```
tccli dlc ListApiKeys --cli-unfold-argument  \
    --Page 1 \
    --PageSize 200 \
    --StartTime 1781523096437 \
    --EndTime 1781523996437 \
    --Filters.0.Name Keyword \
    --Filters.0.Operator LIKE \
    --Filters.0.Values xgboost-self-scale-test \
    --SortFields.0.Field CreateTime \
    --SortFields.0.Order DESC
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
        "RequestId": "c0d08fc7-d173-4b34-9946-ed5c512a507b"
    }
}
```

