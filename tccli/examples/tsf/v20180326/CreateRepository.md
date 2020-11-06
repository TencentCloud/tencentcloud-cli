**Example 1: 创建仓库**



Input: 

```
tccli tsf CreateRepository --cli-unfold-argument  \
    --RepositoryName xxxxx \
    --RepositoryType private \
    --BucketName mybucket \
    --BucketRegion cq \
    --Directory aa/bb \
    --RepositoryDesc xxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "718bc8d5-ccd5-4735-b6b2-c864661e20bc",
        "Result": true
    }
}
```

