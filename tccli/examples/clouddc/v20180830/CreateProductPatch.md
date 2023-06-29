**Example 1: 产研接口-推送产品补丁包信息接口**

产研侧有补丁包发布时，需要将物料传递到交付侧，目前是采用产研人员手工上传天途的方式，处理效率低下。
因此需要开发产品补丁包接收接口，可以和产研的发布平台对接，发布平台发布完成将产品补丁包推送到天途。
文档链接：https://iwiki.woa.com/pages/viewpage.action?pageId=395934565

Input: 

```
tccli clouddc CreateProductPatch --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "12345",
        "JsonData": "true"
    }
}
```

