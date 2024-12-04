**Example 1: 绑定license**

创建测试license

Input: 

```
tccli vcube CreateTrialLicense --cli-unfold-argument  \
    --ApplicationId 123 \
    --FeatureIds 3
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

