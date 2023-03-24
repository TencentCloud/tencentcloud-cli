**Example 1: 移动媒体到某分类下面**

 

Input: 

```
tccli cme MoveResource --cli-unfold-argument  \
    --Platform test \
    --SourceResource.Resource.Id 123245678 \
    --SourceResource.Resource.Type MATERIAL \
    --SourceResource.Owner.Id 6b6ef043-85f3-4614-b735-768bb466ae5b \
    --SourceResource.Owner.Type PERSON \
    --DestinationResource.Resource.Id /个人/视频 \
    --DestinationResource.Resource.Type CLASS \
    --DestinationResource.Owner.Id 6b6ef043-85f3-4614-b735-768bb466ae5b \
    --DestinationResource.Owner.Type PERSON
```

Output: 
```
{
    "Response": {
        "RequestId": "d1c5eb0e-e499-4419-b465-60c0973b3d2"
    }
}
```

**Example 2: 移动分类到不存在的分类下，资源归属相同**

目标分类不存在，操作结果为将原始分类重命名为 /个人/娱乐

Input: 

```
tccli cme MoveResource --cli-unfold-argument  \
    --Platform test \
    --SourceResource.Resource.Id /个人/综艺 \
    --SourceResource.Resource.Type CLASS \
    --SourceResource.Owner.Id 6b6ef043-85f3-4614-b735-768bb466ae5b \
    --SourceResource.Owner.Type PERSON \
    --DestinationResource.Resource.Id /个人/娱乐 \
    --DestinationResource.Resource.Type CLASS \
    --DestinationResource.Owner.Id 6b6ef043-85f3-4614-b735-768bb466ae5b \
    --DestinationResource.Owner.Type PERSON
```

Output: 
```
{
    "Response": {
        "RequestId": "d1c5eb0e-e499-4419-b465-60c097fbb65b"
    }
}
```

**Example 3: 移动分类到已经存在的分类下**

目标分类已经存在，操作结果为将原始分类的资源移到新分类 /个人/娱乐/综艺

Input: 

```
tccli cme MoveResource --cli-unfold-argument  \
    --Platform test \
    --SourceResource.Resource.Id /个人/综艺 \
    --SourceResource.Resource.Type CLASS \
    --SourceResource.Owner.Id 6b6ef043-85f3-4614-b735-768bb466ae5b \
    --SourceResource.Owner.Type PERSON \
    --DestinationResource.Resource.Id /个人/娱乐 \
    --DestinationResource.Resource.Type CLASS \
    --DestinationResource.Owner.Id 6b6ef043-85f3-4614-b735-768bb466ae5b \
    --DestinationResource.Owner.Type PERSON
```

Output: 
```
{
    "Response": {
        "RequestId": "d1c5eb0e-e499-4419-b465-60c097fbb65b"
    }
}
```

**Example 4: 跨归属移动媒体**

将归属于个人的媒体文件移动到团队

Input: 

```
tccli cme MoveResource --cli-unfold-argument  \
    --Platform test \
    --SourceResource.Resource.Id 123245678 \
    --SourceResource.Resource.Type MATERIAL \
    --SourceResource.Owner.Id 6b6ef043-85f3-4614-b735-xxx \
    --SourceResource.Owner.Type PERSON \
    --DestinationResource.Resource.Id /个人/视频 \
    --DestinationResource.Resource.Type CLASS \
    --DestinationResource.Owner.Id cmetid_5fa4f63306e69dxx \
    --DestinationResource.Owner.Type TEAM
```

Output: 
```
{
    "Response": {
        "RequestId": "d1c5eb0e-e499-4419-b465-60c097fbb65b"
    }
}
```

