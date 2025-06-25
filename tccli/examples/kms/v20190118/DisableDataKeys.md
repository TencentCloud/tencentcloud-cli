**Example 1: 批量禁用数据密钥示例**



Input: 

```
tccli kms DisableDataKeys --cli-unfold-argument  \
    --DataKeyIds 7fe31abf-5018-11f0-b672-52540073b995 8042dfcb-5018-11f0-b672-52540073b995
```

Output: 
```
{
    "Response": {
        "RequestId": "1b4bfd47-df00-4494-9131-da3870a76295"
    }
}
```

