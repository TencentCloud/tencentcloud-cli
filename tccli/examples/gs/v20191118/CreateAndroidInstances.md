**Example 1: CreateAndroidInstances**



Input: 

```
tccli gs CreateAndroidInstances --cli-unfold-argument  \
    --Zone abc \
    --Type abc \
    --Number 1
```

Output: 
```
{
    "Response": {
        "AndroidInstanceIds": [
            "abc",
            "def",
            "hij"
        ],
        "RequestId": "5f21d5f7-6f2e-4bb6-8124-c7918db7d868"
    }
}
```

