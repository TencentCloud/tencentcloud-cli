**Example 1: 发起获取媒体文件属性任务**

对 FileId 为 5285485487985271487 的文件发起获取媒体文件属性任务。

Input: 

```
tccli vod DescribeFileAttributes --cli-unfold-argument  \
    --FileId 5285485487985271487
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-DescribeFileAttributes-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

