**Example 1: 修改对象存储备注**



Input: 

```
tccli csip ModifyCosMarkInfo --cli-unfold-argument  \
    --BucketNameSet.0.AppId 1357673452 \
    --BucketNameSet.0.BucketName brainzs-1357673452 \
    --MarkInfo 安全通
```

Output: 
```
{
    "Response": {
        "RequestId": "6a625df7-dea0-4ba2-9942-97303d13d23e"
    }
}
```

