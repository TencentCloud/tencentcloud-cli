**Example 1: 创建DID**

创建机构DID

Input: 

```
tccli tdid CreateTDid --cli-unfold-argument  \
    --GroupId 1 \
    --ClusterId bcos-fmtkyt8xne \
    --Relegation 0
```

Output: 
```
{
    "Response": {
        "Did": "did:tdid:1:0xdab41eb32082044366f1b5712504d0b623b095c1",
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

