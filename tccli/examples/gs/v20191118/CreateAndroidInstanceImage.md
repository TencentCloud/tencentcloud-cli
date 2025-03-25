**Example 1: 创建安卓实例镜像**

创建安卓实例镜像

Input: 

```
tccli gs CreateAndroidInstanceImage --cli-unfold-argument  \
    --AndroidInstanceId cai-abcd1234 \
    --AndroidInstanceImageName test-image
```

Output: 
```
{
    "Response": {
        "RequestId": "6f7b34a3-0c00-4fac-b6f0-08d47ac3e736",
        "AndroidInstanceImageId": "image-abc"
    }
}
```

