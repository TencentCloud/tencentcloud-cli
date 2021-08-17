**Example 1: 创建分散置放群组**

创建分散置放群组

Input: 

```
tccli cvm CreateDisasterRecoverGroup --cli-unfold-argument  \
    --Name 物理机容灾组 \
    --Type HOST
```

Output: 
```
{
    "Response": {
        "Type": "HOST",
        "DisasterRecoverGroupId": "ps-qajfd25h",
        "Name": "物理机容灾组",
        "CvmQuotaTotal": 50,
        "CurrentNum": 0,
        "CreateTime": "2020-09-22 00:00:00",
        "RequestId": "21387009-9b9c-4b57-8fa2-8228f702ff6c"
    }
}
```

