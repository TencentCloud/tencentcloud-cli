**Example 1: 更新凭据内容**



Input: 

```
tccli ssm UpdateSecret --cli-unfold-argument  \
    --SecretName test \
    --VersionId v1.0 \
    --SecretString 'new value'
```

Output: 
```
{
    "Response": {
        "RequestId": "e6993612-6922-4f2d-bb36-37348f36eba5",
        "SecretName": "test",
        "VersionId": "v2.0"
    }
}
```

