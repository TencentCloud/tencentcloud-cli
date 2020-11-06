**Example 1: Applying for stream mix — using template 40**

This example shows you how to use a preset stream mix template to mix streams.

Input: 

```
tccli live CreateCommonMixStream --cli-unfold-argument  \
    --MixStreamSessionId test_room \
    --MixStreamTemplateId 40 \
    --OutputParams.OutputStreamName test_stream1 \
    --InputStreamList.0.InputStreamName test_stream1 \
    --InputStreamList.0.LayoutParams.ImageLayer 1 \
    --InputStreamList.1.InputStreamName test_stream2 \
    --InputStreamList.1.LayoutParams.ImageLayer 2
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: Applying for stream mix — using custom layout parameters**

This example shows you how to use a custom layout.

Input: 

```
tccli live CreateCommonMixStream --cli-unfold-argument  \
    --MixStreamSessionId test_room \
    --OutputParams.OutputStreamName test_stream1 \
    --InputStreamList.0.InputStreamName test_stream1 \
    --InputStreamList.0.LayoutParams.ImageLayer 1 \
    --InputStreamList.0.LayoutParams.ImageWidth  ' 1280' \
    --InputStreamList.0.LayoutParams.ImageHeight ' 720' \
    --InputStreamList.1.InputStreamName test_stream2 \
    --InputStreamList.1.LayoutParams.ImageLayer 2 \
    --InputStreamList.1.LayoutParams.ImageWidth  ' 240' \
    --InputStreamList.1.LayoutParams.ImageHeight ' 320' \
    --InputStreamList.1.LayoutParams.LocationX ' 100' \
    --InputStreamList.1.LayoutParams.LocationY ' 100'
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 3: Applying for stream mix — using cropping parameters**

This example shows you how to use cropping parameters.

Input: 

```
tccli live CreateCommonMixStream --cli-unfold-argument  \
    --MixStreamSessionId test_room \
    --OutputParams.OutputStreamName test_stream1 \
    --InputStreamList.0.InputStreamName test_stream1 \
    --InputStreamList.0.LayoutParams.ImageLayer 1 \
    --InputStreamList.0.LayoutParams.ImageWidth  ' 1280' \
    --InputStreamList.0.LayoutParams.ImageHeight ' 720' \
    --InputStreamList.1.InputStreamName test_stream2 \
    --InputStreamList.1.LayoutParams.ImageLayer 2 \
    --InputStreamList.1.LayoutParams.ImageWidth  ' 240' \
    --InputStreamList.1.LayoutParams.ImageHeight ' 320' \
    --InputStreamList.1.LayoutParams.LocationX ' 100' \
    --InputStreamList.1.LayoutParams.LocationY ' 100' \
    --InputStreamList.1.CropParams.CropWidth ' 240' \
    --InputStreamList.1.CropParams.CropHeight ' 320' \
    --InputStreamList.1.CropParams.CropStartLocationX ' 100' \
    --InputStreamList.1.CropParams.CropStartLocationY ' 100'
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

