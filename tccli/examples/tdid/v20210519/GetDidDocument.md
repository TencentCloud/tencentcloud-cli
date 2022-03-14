**Example 1: GetDidDocument**

查看DID文档

Input: 

```
tccli tdid GetDidDocument --cli-unfold-argument  \
    --Did did:tdid:1:0xa75368ab6ab9cb6d01e81d22155279ee4eca3f4d
```

Output: 
```
{
    "Response": {
        "Name": "test",
        "Document": "aaa",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

