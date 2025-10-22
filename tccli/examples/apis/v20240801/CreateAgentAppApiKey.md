**Example 1: 创建app的apiKey**

创建app的apiKey

Input: 

```
tccli apis CreateAgentAppApiKey --cli-unfold-argument  \
    --ID aga-71702335 \
    --InstanceID ins-e6fbc9b9
```

Output: 
```
{
    "Response": {
        "Data": {
            "ApiKey": "sk-5846e48d04C55509a4449e2f4DF95CC0"
        },
        "RequestId": "890a8922-9a2d-4fba-82e2-58c89fd7d92b"
    }
}
```

