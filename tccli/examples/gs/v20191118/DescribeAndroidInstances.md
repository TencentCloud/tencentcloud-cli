**Example 1: 查询安卓实例**

查询安卓实例

Input: 

```
tccli gs DescribeAndroidInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 100 \
    --AndroidInstanceIds xx \
    --AndroidInstanceRegion xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "6f7b34a3-0c00-4fac-b6f0-08d47ac3e736",
        "TotalCount": 1,
        "AndroidInstances": [
            {
                "AndroidInstanceId": "xxx",
                "AndroidInstanceRegion": "ap-guagnzhou",
                "State": "xxx",
                "AndroidInstanceType": "xxx"
            }
        ]
    }
}
```

