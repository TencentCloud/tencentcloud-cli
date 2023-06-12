**Example 1: 创建目标组**

创建目标组

Input: 

```
tccli clb CreateTargetGroup --cli-unfold-argument  \
    --VpcId vpc-i1cnjuhx \
    --Port 80 \
    --TargetGroupName czhtest
```

Output: 
```
{
    "Response": {
        "TargetGroupId": "lbtg-81******",
        "RequestId": "9a4096dd-45a1-4e03-be8e-482a2fb48b59"
    }
}
```

