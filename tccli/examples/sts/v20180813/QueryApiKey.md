**Example 1: 拉取API密钥列表**



Input: 

```
tccli sts QueryApiKey --cli-unfold-argument  \
    --TargetUin 123456
```

Output: 
```
{
    "Response": {
        "idKeys": [
            {
                "secretId": "xxxxxx",
                "createTime": 1575517111,
                "status": 1
            }
        ],
        "RequestId": ""
    }
}
```

