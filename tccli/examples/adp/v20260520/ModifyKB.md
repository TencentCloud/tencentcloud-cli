**Example 1: 修改知识库**

修改知识库

Input: 

```
tccli adp ModifyKB --cli-unfold-argument  \
    --KbId 2095346479588688512 \
    --Spec.Description 测试编辑 \
    --Spec.EsConfig.EncryptedPassword WG1MFdZ8blowOUfmgYdcRZrN0jUR0qbO2MT4ZkjsNYDkVZra4Y0cA0+BCVe7+mJh07fPBqGn12QivpFACZ7Yt9oALjEMeEznjmW6YKRCwt3AaZ5l6liiCuFhO3x1DfWEr0kTb2acxVGYw40cv5QdivoSu+bLtcF8XATIT3KEeAuUAmBEsd2rWLWpKQAwVCxRSskO3TA2hy+mMtYa8ERLhELn9bDMRahrY2tcLK0Wl+5ji1aZuDBp/4z/KhOLVtpvg87tcd6rGY5WWhIStAgBoQs5XsBHMDZKCDapKWKmpXBLJKViBE9LQhRXDNLRvikwO0v1/pcjmoy++7nFaJAmBQ== \
    --Spec.EsConfig.InstanceId  \
    --Spec.EsConfig.StorageType 2 \
    --Spec.EsConfig.UserName  \
    --Spec.ModelConfig.EmbeddingModel Youtu/youtu-embedding-llm \
    --Spec.ModelConfig.QaExtractModel Deepseek/deepseek-v4-pro \
    --Spec.Name 测试编辑 \
    --UpdateMask.Paths name
```

Output: 
```
{
    "Response": {
        "RequestId": "18174358-c58e-4c2a-baf4-0bfebd539f16"
    }
}
```

