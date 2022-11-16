**Example 1: GetPublicKey**

查看公钥

Input: 

```
tccli tdid GetPublicKey --cli-unfold-argument  \
    --Did xx
```

Output: 
```
{
    "Response": {
        "Did": "xx",
        "PublicKey": "xx",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

