**Example 1: CreateTokenPlanApiKeys**



Input: 

```
tccli tokenhub CreateTokenPlanApiKeys --cli-unfold-argument  \
    --TeamId team-3a834f2dbcf48840115cbf4b48f25342 \
    --ApiKeyName syytest-1 \
    --Count 2 \
    --AllowedModels glm-5
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ApiKeyId": "ak-tp-20260412-b2ddcfeb599f8345cb7ad22c370b1acd"
            },
            {
                "ApiKeyId": "ak-tp-20260412-c727346e6086cc5c5594b40786957aa1"
            }
        ],
        "RequestId": "2c146814-7ca2-494b-8d09-2f4cc6cef3a2"
    }
}
```

