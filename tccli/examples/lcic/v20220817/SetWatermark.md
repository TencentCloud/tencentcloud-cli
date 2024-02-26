**Example 1: 示例**

设置水印

Input: 

```
tccli lcic SetWatermark --cli-unfold-argument  \
    --SdkAppId 123333 \
    --TeacherUrl https://tcic-backend-record-22112222.cos.ap-beujing.myqcloud.com/teacher-02_219090_210001.png \
    --BoardUrl https://tcic-backend-record-22112222.cos.ap-beujing.myqcloud.com/board-02_219090_210001.png \
    --VideoUrl https://tcic-backend-record-22112222.cos.ap-beujing.myqcloud.com/video-02_219090_210001.png \
    --BoardW 0 \
    --BoardH 0 \
    --BoardX 50 \
    --BoardY 50 \
    --TeacherW 0 \
    --TeacherH 0 \
    --TeacherX 50 \
    --TeacherY 50 \
    --Text 文本内容 \
    --TextColor 黑
```

Output: 
```
{
    "Response": {
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

