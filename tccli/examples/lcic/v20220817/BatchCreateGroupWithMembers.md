**Example 1: 批量创建群组**

批量创建群组

Input: 

```
tccli lcic BatchCreateGroupWithMembers --cli-unfold-argument  \
    --SdkAppId 12345678 \
    --GroupBaseInfos.0.GroupName test1 \
    --GroupBaseInfos.0.TeacherId 2i5WfUzRRC2Eb2uNmLNv96gzxCv \
    --GroupBaseInfos.1.GroupName test2 \
    --MemberIds 2d3FgsZRRB2EbRu5Cwe8Rd7R6Bc 2aiT64yygupUJ5zrkRi2r3hh54x
```

Output: 
```
{
    "Response": {
        "GroupIds": [
            "2CvDgjRNjylAs",
            "BZB4iZc0F6ko"
        ],
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

