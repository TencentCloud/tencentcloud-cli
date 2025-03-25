**Example 1: CreateAndroidInstances**



Input: 

```
tccli gs CreateAndroidInstances --cli-unfold-argument  \
    --Zone ap-shenzhen-1 \
    --Type A6 \
    --Number 1
```

Output: 
```
{
    "Response": {
        "AndroidInstanceIds": [
            "cai-abcd1234",
            "cai-abcd1235",
            "cai-abcd1236"
        ],
        "RequestId": "5f21d5f7-6f2e-4bb6-8124-c7918db7d868"
    }
}
```

