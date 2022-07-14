**Example 1: 新建量产 - 系统生成**

使用系统生成的方式进行量产

Input: 

```
tccli iotexplorer CreateBatchProduction --cli-unfold-argument  \
    --ProjectId prj-pq00mstg \
    --BurnMethod 0 \
    --BatchCnt 5 \
    --GenerationMethod 0 \
    --ProductId R32ONVL0EU
```

Output: 
```
{
    "Response": {
        "BatchProductionId": "LC-74ais6a3",
        "ProductId": "R32ONVL0EU",
        "ProjectId": "prj-pq00mstg",
        "RequestId": "rest-client2213121026"
    }
}
```

**Example 2: 新建量产 - 上传URL**

使用上传文件 url 的方式进行量产

Input: 

```
tccli iotexplorer CreateBatchProduction --cli-unfold-argument  \
    --ProjectId prj-pq00mstg \
    --BurnMethod 0 \
    --UploadUrl www.xxxxxxxx.com/xxxxxx.csv \
    --GenerationMethod 1 \
    --ProductId R32ONVL0EU
```

Output: 
```
{
    "Response": {
        "BatchProductionId": "LC-74ais6a3",
        "ProductId": "R32ONVL0EU",
        "ProjectId": "prj-pq00mstg",
        "RequestId": "rest-client3331231026"
    }
}
```

