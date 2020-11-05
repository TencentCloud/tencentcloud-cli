**Example 1: Clipping a file in VOD to generate a new video**

This example shows you how to clip the 60th to 120th seconds of video `5285485487985271487` to generate a new VOD video.

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType File\
    --FileInfos.0.FileId 5285485487985271487\
    --FileInfos.0.StartTimeOffset 60.0\
    --FileInfos.0.EndTimeOffset 120.0
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-clipMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 2: Splicing multiple streams in VOD to generate a new video**

This example shows you how to splice three LVB recording streams whose IDs are 99873, 99874, and 99875 to generate a new VOD video.

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType Stream\
    --StreamInfos.0.StreamId 99873\
    --StreamInfos.1.StreamId 99874\
    --StreamInfos.2.StreamId 99875
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-clipMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 3: Clipping a stream in VOD to generate a new video**

This example shows you how to clip the segment between 10:00:00 and 11:00:00 on September 20, 2018 of the LVB recording stream whose ID is 99873 to generate a new VOD video.

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType Stream\
    --StreamInfos.0.StreamId 99873\
    --StreamInfos.0.StartTime 2018-09-20T11:00:00Z
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-clipMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 4: Directly generating a new video from a stream in VOD**

This example shows you how to generate a new VOD video from LVB recording stream whose ID is 99873.

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType Stream\
    --StreamInfos.0.StreamId 99873
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-clipMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 5: Clipping multiple files in VOD and then splicing the clips to generate a new video**

This example shows you how to clip and splice the 60th to 120th seconds of videos `5285485487985271487`, `5285485487985271488`, and `5285485487985271489` respectively to generate a new VOD video.

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType File\
    --FileInfos.0.FileId 5285485487985271487\
    --FileInfos.0.StartTimeOffset 60.0\
    --FileInfos.0.EndTimeOffset 120.0\
    --FileInfos.1.FileId 5285485487985271488\
    --FileInfos.1.StartTimeOffset 60.0\
    --FileInfos.1.EndTimeOffset 120.0\
    --FileInfos.2.FileId 5285485487985271489\
    --FileInfos.2.StartTimeOffset 60.0\
    --FileInfos.2.EndTimeOffset 120.0
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-clipMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 6: Clipping a file in VOD to generate a new video and run a task flow**

This example shows you how to clip the 60th to 120th seconds of video `5285485487985271487` to generate a new VOD video and run task flow `TranscodeAndSnapshot`.

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType File\
    --FileInfos.0.FileId 5285485487985271487\
    --FileInfos.0.StartTimeOffset 60.0\
    --FileInfos.0.EndTimeOffset 120.0\
    --ProcedureName TranscodeAndSnapshot
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-clipMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 7: Clipping multiple streams in VOD and then splicing the clips to generate a new video**

This example shows you how to clip the segments between 10:00:00 and 11:00:00 on September 20, 2018 of three LVB recording streams whose IDs are 99873, 99874, and 99875 and splice them to generate a new VOD video.

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType Stream\
    --StreamInfos.0.StreamId 99873\
    --StreamInfos.0.StartTime 2018-09-20T11:00:00Z\
    --StreamInfos.1.StreamId 99874\
    --StreamInfos.1.StartTime 2018-09-20T11:00:00Z\
    --StreamInfos.2.StreamId 99875\
    --StreamInfos.2.StartTime 2018-09-20T11:00:00Z
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-clipMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 8: Splicing multiple files in VOD to generate a new video**

This example shows you how to splice videos `5285485487985271487`, `5285485487985271488`, and `5285485487985271489` to generate a new VOD video.

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType File\
    --FileInfos.0.FileId 5285485487985271487\
    --FileInfos.1.FileId 5285485487985271488\
    --FileInfos.2.FileId 5285485487985271489
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-clipMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

