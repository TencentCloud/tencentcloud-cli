**Example 1: 获取镜像信息**

获取镜像信息

Input: 

```
tccli tke DescribeImages --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ImageInstanceSet": [
            {
                "Alias": "Tencent Linux 2.2 64bit (tkernel3)",
                "OsCustomizeType": "GENERAL",
                "OsName": "tlinux2.2(tkernel3)x86_64",
                "ImageId": "img-2lr9q49h"
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459398"
    }
}
```

