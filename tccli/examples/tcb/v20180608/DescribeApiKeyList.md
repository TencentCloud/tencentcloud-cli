**Example 1: 查询API Key列表**



Input: 

```
tccli tcb DescribeApiKeyList --cli-unfold-argument  \
    --EnvId env-123 \
    --PageNumber 1 \
    --PageSize 10 \
    --KeyType api_key
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "ApiKey": "agKSFS******jKdhas",
                "CreateAt": "2026-02-19T14:25:17+08:00",
                "ExpireAt": "2026-03-19T14:25:17+08:00",
                "KeyId": "akdj3jsk3112ks",
                "Name": "example_key"
            }
        ],
        "Total": 1,
        "RequestId": "13ef3988-16d7-48b5-91b8-505e35ea51b3"
    }
}
```

