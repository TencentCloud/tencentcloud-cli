**Example 1: 创建Goosefsx文件系统**



Input: 

```
tccli goosefs CreateFileSystem --cli-unfold-argument  \
    --Name ai_fs \
    --Description our test fs \
    --VpcId vpc-lc0aecbo \
    --SubnetId subnet-jwtwc1vj \
    --Zone ap-beijing-7 \
    --GooseFSxBuildElements.Model C60 \
    --GooseFSxBuildElements.Capacity 4608
```

Output: 
```
{
    "Response": {
        "FileSystemId": "x-c60-ewe600t4",
        "RequestId": "1207751e-b9a8-40f2-ae9b-122c518fbb9a"
    }
}
```

