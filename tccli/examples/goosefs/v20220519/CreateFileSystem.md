**Example 1: 创建文件系统**

创建文件系统

Input: 

```
tccli goosefs CreateFileSystem --cli-unfold-argument  \
    --VpcId vpc-a1b2c3d4 \
    --Name ai_test_fs \
    --Zone ap-guangzhou-3 \
    --Tag.0.Value ai_team \
    --Tag.0.Key owner_group \
    --Tag.1.Value test \
    --Tag.1.Key env \
    --SubnetId subnet-m1n1g1h1 \
    --Type goosefsx \
    --GooseFSxBuildElements.Model c60 \
    --GooseFSxBuildElements.Capacity 4608 \
    --GooseFSxBuildElements.MappedBucketList.0.BucketName mybucket2-12500000 \
    --GooseFSxBuildElements.MappedBucketList.0.FileSystemPath / \
    --GooseFSxBuildElements.MappedBucketList.1.BucketName mybucket1-12500000 \
    --GooseFSxBuildElements.MappedBucketList.1.FileSystemPath / \
    --GooseFSxBuildElements.MappedBucketList.2.BucketName mybucket3-12500000 \
    --GooseFSxBuildElements.MappedBucketList.2.FileSystemPath /xxx \
    --Description ai team test only
```

Output: 
```
{
    "Response": {
        "RequestId": "b3caa32f-5e39-4360-91e4-5724369b78a6"
    }
}
```

