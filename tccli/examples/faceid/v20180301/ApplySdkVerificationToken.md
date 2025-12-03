**Example 1: ApplySdkVerificationToken调用示例**



Input: 

```
tccli faceid ApplySdkVerificationToken --cli-unfold-argument  \
    --CheckMode 1 \
    --SecurityLevel 4 \
    --IdCardType HK \
    --CompareImage /9j/4AAQSkZJRg.....s97n//2Q== \
    --DisableChangeOcrResult True \
    --DisableCheckOcrWarnings True \
    --SdkVersion ENHANCED \
    --ActionList blink \
    --AllowExpiredDocument False
```

Output: 
```
{
    "Response": {
        "SdkToken": "65474840-81919-014342-85A1-1F2B3E3DC7BF",
        "RequestId": "319f2c60-09db-4120-aedb-90579e3f430a"
    }
}
```

