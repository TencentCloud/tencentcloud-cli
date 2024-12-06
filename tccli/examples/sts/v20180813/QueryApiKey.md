**Example 1: 拉取API密钥列表**



Input: 

```
tccli sts QueryApiKey --cli-unfold-argument  \
    --TargetUin 100020328651
```

Output: 
```
{
    "Response": {
        "IdKeys": [
            {
                "SecretId": "AKID***",
                "CreateTime": 1575517111,
                "Status": 2
            }
        ],
        "RequestId": "5cf9d558-a46a-4ce7-bbc2-500cad68b0da"
    }
}
```

