**Example 1: RegisterIssuer**

注册为权威机构

Input: 

```
tccli tdid RegisterIssuer --cli-unfold-argument  \
    --Did did:tdid:1:0xa75368ab6ab9cb6d01e81d22155279ee4eca3f4d \
    --Name aaa \
    --Description mark一下
```

Output: 
```
{
    "Response": {
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

