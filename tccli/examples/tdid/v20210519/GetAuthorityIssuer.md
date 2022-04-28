**Example 1: GetAuthorityIssuer**

获取权威机构信息

Input: 

```
tccli tdid GetAuthorityIssuer --cli-unfold-argument  \
    --Did did:tdid:1:0xa75368ab6ab9cb6d01e81d22155279ee4eca3f4d
```

Output: 
```
{
    "Response": {
        "Did": "",
        "Name": "test",
        "ClusterId": "bcos-ch0wjx6ub4",
        "GroupId": 2,
        "Remark": "",
        "RegisterTime": "2022-02-28 17:58:32",
        "RecognizeTime": "2022-02-28 17:58:32",
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

