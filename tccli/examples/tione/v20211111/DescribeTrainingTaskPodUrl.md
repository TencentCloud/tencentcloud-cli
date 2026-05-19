**Example 1: 查询Pod的URL**



Input: 

```
tccli tione DescribeTrainingTaskPodUrl --cli-unfold-argument  \
    --PodName train-51c30e6fbe1000-36xslo3d8e0w-launcher
```

Output: 
```
{
    "Response": {
        "PodUrl": "train-51c30e6fbe1000-36xslo3d8e0w-launcher.ap-nanjing.tencent.com",
        "RequestId": "fdsafds-fdsafd"
    }
}
```

