**Example 1: DeployByName**

通过Name部署TDID合约

Input: 

```
tccli tdid DeployByName --cli-unfold-argument  \
    --ApplicationName 测试应用11 \
    --ClusterId bcos-fmtkyt8xne \
    --GroupId 1
```

Output: 
```
{
    "Response": {
        "Hash": "0x1c0eb253d21cbe557573e6deba44a07acedfc16176f72c9a9c3f016e517c6e4b",
        "RequestId": "41a9acae-cef4-4949-b144-48c65ad5e425"
    }
}
```

