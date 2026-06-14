**Example 1: 示例**

示例

Input: 

```
tccli dataagent QueryKnowledgeTask --cli-unfold-argument  \
    --InstanceId dataagent-haBKQxLt \
    --KnowledgeBaseId klbase-XPJwWgiLZv \
    --FileIds de1c7e8b-ace4-4d1f-8b2c-953d67a0128c
```

Output: 
```
{
    "Response": {
        "FileList": [
            {
                "ErrorMsg": "",
                "FileId": "de1c7e8b-ace4-4d1f-8b2c-953d67a0128c",
                "IsTerminated": 1,
                "Status": 1
            }
        ],
        "RequestId": "280fb560-6175-497c-8e00-d7ca0104a6e2"
    }
}
```

