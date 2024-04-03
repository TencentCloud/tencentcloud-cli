**Example 1: 申请混流-使用模板40**

使用混流预置模板混流。

Input: 

```
tccli live CreateCommonMixStream --cli-unfold-argument  \
    --MixStreamTemplateId 40 \
    --MixStreamSessionId test_room \
    --InputStreamList.0.LayoutParams.ImageLayer 1 \
    --InputStreamList.0.InputStreamName test_stream1 \
    --InputStreamList.1.LayoutParams.ImageLayer 2 \
    --InputStreamList.1.InputStreamName test_stream2 \
    --OutputParams.OutputStreamName test_stream1
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 申请混流-使用裁剪参数**

使用裁剪参数。

Input: 

```
tccli live CreateCommonMixStream --cli-unfold-argument  \
    --InputStreamList.0.LayoutParams.ImageLayer 1 \
    --InputStreamList.0.LayoutParams.ImageHeight 720 \
    --InputStreamList.0.LayoutParams.ImageWidth 1280 \
    --InputStreamList.0.InputStreamName test_stream1 \
    --InputStreamList.1.LayoutParams.ImageLayer 2 \
    --InputStreamList.1.LayoutParams.ImageHeight 320 \
    --InputStreamList.1.LayoutParams.ImageWidth 240 \
    --InputStreamList.1.LayoutParams.LocationX 100 \
    --InputStreamList.1.LayoutParams.LocationY 100 \
    --InputStreamList.1.InputStreamName test_stream2 \
    --InputStreamList.1.CropParams.CropWidth 240 \
    --InputStreamList.1.CropParams.CropHeight 320 \
    --InputStreamList.1.CropParams.CropStartLocationX 100 \
    --InputStreamList.1.CropParams.CropStartLocationY 100 \
    --OutputParams.OutputStreamName test_stream1 \
    --MixStreamSessionId test_room
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 3: 申请混流-使用自定义布局参数**

使用自定义布局。

Input: 

```
tccli live CreateCommonMixStream --cli-unfold-argument  \
    --InputStreamList.0.LayoutParams.ImageLayer 1 \
    --InputStreamList.0.LayoutParams.ImageHeight 720 \
    --InputStreamList.0.LayoutParams.ImageWidth 1280 \
    --InputStreamList.0.InputStreamName test_stream1 \
    --InputStreamList.1.LayoutParams.ImageLayer 2 \
    --InputStreamList.1.LayoutParams.ImageHeight 320 \
    --InputStreamList.1.LayoutParams.ImageWidth 240 \
    --InputStreamList.1.LayoutParams.LocationX 100 \
    --InputStreamList.1.LayoutParams.LocationY 100 \
    --InputStreamList.1.InputStreamName test_stream2 \
    --OutputParams.OutputStreamName test_stream1 \
    --MixStreamSessionId test_room
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

