**Example 1: 获取SCIM同步状态**

获取SCIM同步状态

Input: 

```
tccli organization GetSCIMSynchronizationStatus --cli-unfold-argument  \
    --ZoneId z-vft38p2hq8tq
```

Output: 
```
{
    "Response": {
        "RequestId": "a9c83496-1656-4e86-88ba-4cbc26bef4ba",
        "SCIMSynchronizationStatus": "Disabled"
    }
}
```

