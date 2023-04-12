**Example 1: 获取Token**

	
获取 SDK 核验 token

Input: 

```
tccli faceid GetFaceIdTokenIntl --cli-unfold-argument  \
    --CheckMode liveness \
    --SecureLevel 4 \
    --Extra idxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "c27f8a53-1766-4d62-84fc-c400843e9e21",
        "SdkToken": "91BF5AD0-C5C9-41CC-9562-DB35BBA2712D"
    }
}
```

