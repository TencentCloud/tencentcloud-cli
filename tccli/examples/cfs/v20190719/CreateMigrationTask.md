**Example 1: 创建迁移任务**

用于创建数据迁移任务

Input: 

```
tccli cfs CreateMigrationTask --cli-unfold-argument  \
    --BucketRegion ap-nanjing \
    --SrcService COS \
    --CoverType 1 \
    --SrcSecretKey ***************************** \
    --BucketPath cos/ \
    --MigrationMode 0 \
    --FileSystemId cfs-8dd58fd7 \
    --BucketName test-1-1256238147 \
    --FsPath /test/ \
    --MigrationType 0 \
    --TaskName test \
    --SrcSecretId ************************************************** \
    --FsName test
```

Output: 
```
{
    "Response": {
        "TaskId": "cfsmigrate-dfe9b1f2",
        "RequestId": "91cd4a08-a105-4c59-b229-82f0fs7363b8"
    }
}
```

