**Example 1: 查询导播台备播状态**

查询导播台备播状态

Input: 

```
tccli live DescribeCasterEmergencyStatus --cli-unfold-argument  \
    --CasterId 63501
```

Output: 
```
{
    "Response": {
        "EmergencyStatus": 1,
        "RequestId": "84fea7c5-37e7-4d89-ba04-76338dc7b41d"
    }
}
```

