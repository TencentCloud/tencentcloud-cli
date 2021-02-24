**Example 1: 查询黑名单文件列表**



Input: 

```
tccli cr QueryBlackListData --cli-unfold-argument  \
    --Module AiApi \
    --Operation QueryBlackListData
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Data": [
            {
                "OperType": "xx",
                "BlackValidDate": "2020-09-22",
                "BlackDescription": "xx",
                "BlackType": "xx",
                "BlackValue": "xx",
                "BlackAddDate": "2020-09-22"
            }
        ],
        "RequestId": "xx"
    }
}
```

