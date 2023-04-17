**Example 1: 获取存储桶列表**

用于获取对象存储桶列表

Input: 

```
tccli cfs DescribeBucketList --cli-unfold-argument  \
    --SrcSecretId ****************************** \
    --SrcSecretKey ***************************** \
    --SrcService COS
```

Output: 
```
{
    "Response": {
        "BucketList": [
            {
                "Name": "1-1256238147",
                "Region": "ap-nanjing"
            }
        ],
        "TotalCount": 1,
        "RequestId": "ea7fe4ad-d508-41f9-bcc7-6e043102b5ba"
    }
}
```

