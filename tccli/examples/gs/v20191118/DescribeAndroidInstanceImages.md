**Example 1: 查询安卓实例镜像**

查询安卓实例镜像

Input: 

```
tccli gs DescribeAndroidInstanceImages --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "AndroidInstanceImages": [
            {
                "AndroidInstanceImageId": "image-abc",
                "AndroidInstanceImageName": "imagetestname",
                "AndroidInstanceImageState": "NORMAL"
            }
        ],
        "RequestId": "requestid"
    }
}
```

