**Example 1: 获取上传文件授权信息，并根据信息进行文件的上传**

下面是请求返回的授权信息：

```
{
    "Response": {
    	"BucketAuth": "q-sign-algorithm=sha1&q-ak=AKID0ndxGAMVRNGyKXulw5ilRyyxWwBKtEQa&q-sign-time=1571902453;1571902813&q-key-time=1571902453;1571902813&q-header-list=host&q-url-param-list=&q-signature=93dbff22e6b80fb5907fe5f4e31a491p7f146cee",
        "BucketName": "xxxx",
        "AssetRegion": "ap-shanghai",
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad81"
    }
}
```
上传 Bucket ，请求 HOST 地址为：`https://<BucketName>.cos.<AssetRegion>.myqcloud.com`，具体使用方式参考[COS API 文档](https://cloud.tencent.com/document/product/436/7749)，[COS SDK集成](https://cloud.tencent.com/document/product/436/6474) 进行调用。

Input: 

```
tccli gse GetUploadCredentials --cli-unfold-argument  \
    --AssetRegion ap-shanghai \
    --BucketKey server.zip
```

Output: 
```
{
    "Response": {
        "BucketAuth": "q-sign-algorithm=sha1&q-ak=AKID0ndxGAMVRNGyKXulw5ilRyyxWwBKtEQa&q-sign-time=1571902453;1571902813&q-key-time=1571902453;1571902813&q-header-list=host&q-url-param-list=&q-signature=93dbff22e6b80fb5907fe5f4e31a491p7f146cee",
        "BucketName": "xxxx",
        "AssetRegion": "ap-shanghai",
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad81"
    }
}
```

