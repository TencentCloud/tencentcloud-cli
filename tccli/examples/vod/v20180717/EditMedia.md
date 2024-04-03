**Example 1: 对点播中的一个流，直接生成一个新的视频**

对一个 ID 为 99873 的直播录制流，生成一个新的点播视频

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType Stream \
    --StreamInfos.0.StreamId 99873
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 2: 对点播中的一个流进行剪辑，生成一个新的视频**

对一个 ID 为 99873 的直播录制流，剪辑从 2018-09-20 的 10:00:00 到 11:00:00 的片段，生成一个新的点播视频

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType Stream \
    --StreamInfos.0.StreamId 99873 \
    --StreamInfos.0.StartTime 2018-09-20T10:00:00Z \
    --StreamInfos.0.EndTime 2018-09-20T11:00:00Z
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

**Example 3: 对点播中的多个流进行拼接，生成一个新的视频**

将 ID 为 99873，99874 和 99875 的 3 个直播录制流进行拼接，生成一个新的点播视频

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType Stream \
    --StreamInfos.0.StreamId 99873 \
    --StreamInfos.1.StreamId 99874 \
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

**Example 4: 对点播中的一个文件进行剪辑，生成一个新的视频**

对 5285485487985271487 剪辑第 60 秒到 120 秒的片段，生成一个新的点播视频

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType File \
    --FileInfos.0.FileId 5285485487985271487 \
    --FileInfos.0.StartTimeOffset 60.0 \
    --FileInfos.0.EndTimeOffset 120.0
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 5: 对点播中的多个文件进行拼接，生成一个新的视频**

拼接 5285485487985271487，5285485487985271488，5285485487985271489 三个视频，生成一个新的点播视频

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType File \
    --FileInfos.0.FileId 5285485487985271487 \
    --FileInfos.1.FileId 5285485487985271488 \
    --FileInfos.2.FileId 5285485487985271489
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 6: 对点播中的多个流进行剪辑，然后拼接，生成一个新的视频**

将 ID 为 99873，99874 和 99875 的 3 个直播录制流，分别剪辑出从 2018-09-20 的 10:00:00 到 11:00:00 的片段，拼接后生成一个新的点播视频

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType Stream \
    --StreamInfos.0.StreamId 99873 \
    --StreamInfos.0.StartTime 2018-09-20T10:00:00Z \
    --StreamInfos.0.EndTime 2018-09-20T11:00:00Z \
    --StreamInfos.1.StreamId 99874 \
    --StreamInfos.1.StartTime 2018-09-20T10:00:00Z \
    --StreamInfos.1.EndTime 2018-09-20T11:00:00Z \
    --StreamInfos.2.StreamId 99875 \
    --StreamInfos.2.StartTime 2018-09-20T10:00:00Z \
    --StreamInfos.2.EndTime 2018-09-20T11:00:00Z
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

**Example 7: 对点播中的多个文件进行剪辑，然后再拼接，生成一个新的视频**

对 5285485487985271487，5285485487985271488，5285485487985271489 三个视频分别进行剪辑（剪辑第 60 秒到 120 秒的片段），然后拼接，生成一个新的点播视频

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType File \
    --FileInfos.0.FileId 5285485487985271487 \
    --FileInfos.0.StartTimeOffset 60.0 \
    --FileInfos.0.EndTimeOffset 120.0 \
    --FileInfos.1.FileId 5285485487985271488 \
    --FileInfos.1.StartTimeOffset 60.0 \
    --FileInfos.1.EndTimeOffset 120.0 \
    --FileInfos.2.FileId 5285485487985271489 \
    --FileInfos.2.StartTimeOffset 60.0 \
    --FileInfos.2.EndTimeOffset 120.0
```

Output: 
```
{
    "Response": {
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3",
        "TaskId": "125xxx65-EditMedia-bffb15f07530b57bc1aabb01fac74bca"
    }
}
```

**Example 8: 对点播中的一个文件进行剪辑，生成一个新的视频，同时对新视频执行任务流**

对 5285485487985271487 剪辑第 60 秒到 120 秒的片段，生成一个新的点播视频，并执行任务流 TranscodeAndSnapshot

Input: 

```
tccli vod EditMedia --cli-unfold-argument  \
    --InputType File \
    --FileInfos.0.FileId 5285485487985271487 \
    --FileInfos.0.StartTimeOffset 60.0 \
    --FileInfos.0.EndTimeOffset 120.0 \
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

