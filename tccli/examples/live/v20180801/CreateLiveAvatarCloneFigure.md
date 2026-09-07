**Example 1: 创建图片形象克隆**



Input: 

```
tccli live CreateLiveAvatarCloneFigure --cli-unfold-argument  \
    --SceneType PHOTO \
    --FigureName 电子女主播 \
    --MaterialUrl https://wsh-test-1303333058.cos.ap-guangzhou.myqcloud.com/%E7%94%B5%E5%AD%90%E4%BA%A7%E5%93%81%E5%A5%B3%E4%B8%BB%E6%92%AD.png \
    --Gender FEMALE
```

Output: 
```
{
    "Response": {
        "Status": "SUBMITTING",
        "TaskId": "7501977621938212864",
        "RequestId": "08bdc698-230c-491a-a302-520d7eb57b3f"
    }
}
```

