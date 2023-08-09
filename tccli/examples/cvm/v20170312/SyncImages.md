**Example 1: 同步镜像**

同步镜像img-o3ycss2p到广州

Input: 

```
tccli cvm SyncImages --cli-unfold-argument  \
    --ImageIds img-o3ycss2p \
    --DestinationRegions ap-guangzhou
```

Output: 
```
{
    "Response": {
        "ImageSet": [
            {
                "ImageId": "img-o3ycss2p",
                "Region": "ap-guangzhou"
            }
        ],
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

**Example 2: 同步镜像，同时需要返回目的地域的镜像ID**

同步镜像img-o3ycss2p到广州

Input: 

```
tccli cvm SyncImages --cli-unfold-argument  \
    --ImageIds img-o3ycss2p \
    --DestinationRegions ap-guangzhou \
    --ImageSetRequired True
```

Output: 
```
{
    "Response": {
        "ImageSet": [
            {
                "Region": "ap-guangzhou",
                "ImageId": "img-evhmf3fy"
            }
        ],
        "RequestId": "71e69b56-32be-4412-ab45-49eded6a87be"
    }
}
```

