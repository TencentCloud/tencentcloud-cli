**Example 1: 获取API密钥简略信息列表**



Input: 

```
tccli ags DescribeAPIKeyList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "APIKeySet": [
            {
                "CreatedAt": "2025-09-12T14:09:05.242Z",
                "KeyId": "ark-3edcft6y",
                "MaskedKey": "ark_Au****kKjo",
                "Name": "LocalDev",
                "Status": "API_KEY_STATUS_ACTIVE"
            }
        ],
        "TotalCount": 1,
        "RequestId": "37e8ed19-80cd-49f3-9b5a-eaea1bf9c6c1"
    }
}
```

