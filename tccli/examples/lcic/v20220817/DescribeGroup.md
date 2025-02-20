**Example 1: 获取群组详情**

获取群组详情

Input: 

```
tccli lcic DescribeGroup --cli-unfold-argument  \
    --GroupId 2CvDgjRNjylAs \
    --SdkAppId 13465287
```

Output: 
```
{
    "Response": {
        "GroupId": "2CvDgjRNjylAs",
        "GroupName": "myGroup01",
        "TeacherId": "2i5WfUzRRC2Eb2uNmLNv96gzxCv",
        "GroupType": 1,
        "SubGroupIds": [
            "BZB4iZc0F6ko"
        ],
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

