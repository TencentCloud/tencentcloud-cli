**Example 1: 创建app**

创建app

Input: 

```
tccli apis CreateAgentApp --cli-unfold-argument  \
    --InstanceID ins-e6fbc9b9 \
    --Name hello1 \
    --AuthType apiKey
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "aga-2b2e0214"
        },
        "RequestId": "aaa7c5ac-d5fc-4f34-81a0-aeb0af415e28"
    }
}
```

