**Example 1: 执行操作系统转换**

针对实例 ins-6pb6lrmy 执行操作系统转换

Input: 

```
tccli cvm ConvertOperatingSystems --cli-unfold-argument  \
    --InstanceIds ins-6pb6lrmy
```

Output: 
```
{
    "Response": {
        "SupportTargetOSList": [
            {
                "TargetOSType": "TencentOS",
                "TargetOSVersion": "2.4"
            }
        ],
        "TaskId": "12345678",
        "RequestId": "120e85ba-f656-48a7-bdeb-dc17c4fa2xxx"
    }
}
```

