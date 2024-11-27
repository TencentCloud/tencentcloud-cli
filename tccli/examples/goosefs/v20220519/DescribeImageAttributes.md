**Example 1: 示例1**

示例1

Input: 

```
tccli goosefs DescribeImageAttributes --cli-unfold-argument  \
    --DescribeUin 3472213910
```

Output: 
```
{
    "Response": {
        "ImageList": [
            {
                "ClusterUsedFlag": true,
                "DefaultFlag": true,
                "GwUsedFlag": false,
                "ImageId": "img-7rb34bfw",
                "SharedFlag": true,
                "VersionName": "Storage_Scale_Data_Management-5.1.9.1"
            },
            {
                "ClusterUsedFlag": false,
                "DefaultFlag": false,
                "GwUsedFlag": true,
                "ImageId": "img-ipth2mjw",
                "SharedFlag": true,
                "VersionName": "Storage_Scale_Data_Management-5.2.1.0"
            }
        ],
        "RequestId": "442f3f7b-dde7-4542-be10-8cea41fa4df6",
        "TotalCount": 2
    }
}
```

