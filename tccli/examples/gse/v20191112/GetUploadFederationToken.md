**Example 1: 获取生成包上传所需要的临时密钥，根据信息进行文件的上传**

使用临时密钥进行文件上传的场景如下：

1. 准备好上传所需要的 Bucket （这里会初始化相关的 Bucket，只需要用户调用一次，后续直接使用临时密钥上传即可），参见 GetUploadCredentials API 描述。
2. 获取临时密钥请求，参考下面的 GetUploadFederationToken API 示例
3. 调用 COS API 或者集成 COS SDK 进行文件上传，其中大文件，请使用分块上传方式，其中 COS SDK 提供了高级接口上传对象即可，具体细节参考 [COS 文档](https://cloud.tencent.com/document/product/436/14112)。
4. 根据上传成功的 BucketKey 创建 Asset。

Input: 

```
tccli gse GetUploadFederationToken --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AssetCredentials": {
            "TmpSecretId": "xxxx",
            "TmpSecretKey": "yyyy",
            "Token": "jAlJicYVxHStLs34mTFfnSxJ7YpYx2UFae79befda56accd665e0c14b6ea2a8a9qM30cu5FtylTrH9U6Dm89Vl-uZ3vkcIRHS1jA8I9JaMJnAkGDFr-dtMt8v0vO3XSsF_T_RTIQHfqgXpYyyf-mLywmF3kZ07Ub7xIDfQSjGPg9yQXs-nqv2cpnsOLCDTRR598VYgkgExE31vIn6Ca-lNruZhxDwKS1fvi7g75yyLzX0Ambr6sB-ULEF6ubycmuMXyjXM4lsuRCuswkrHxSZXlsYtNF-hLlzcQjU6R4qXO8ncqDxfcVhadCMso_U73RxVcqcH21aG9IlnrLDpYRVGAXpQ1tvsgvOOJBh1mcQV6ef5MVTJFePIUsS7E2Sm1Ivv3-dP1lfHbs-Igu1IyF2hT8-zzs8mFlLt3yfdzwtbBGqZMTW9b-4Y5kdMY-cOqoTxbqjdJKTPEtLwi6160CRaabqSaRKsAI6dhgTsbc2vR4piNvdQZgL8I3vVrRtfAC5a0yZFfmd1EXnJjuYl_ZV78fNBC1VqVWDvWMyckJRZ2TepIItZR26FMkCsbFSTA7m5HN-nvRpo96WVsHy6QeJC9dpZbkHOePDRzZrXLRV_CHjiKn1wozZiNQ2kdDt_j"
        },
        "ExpiredTime": 1597058405,
        "RequestId": "a2b2a551-1551-4625-8ae9-086328d366b7"
    }
}
```

**Example 2: 使用脚本方式快捷上传并且创建 Asset**

为了方便快速地进行文件上传，我们也提供了 Python 脚本（目前只是支持 Linux 和 Mac 系统），您可以[下载](https://uploadasset-1301007756.cos.ap-guangzhou.myqcloud.com/uploadasset.zip)使用

脚本中有详细说明，具体如下：
```
# 该脚本依赖安装如下包：
# 1. tencentcloud-sdk-python
# 2. cos-python-sdk-v5
#
# 如何安装 tencentcloud-sdk-python:
#   pip install tencentcloud-sdk-python
#
# 如何安装 cos-python-sdk-v5:
#  pip install -U cos-python-sdk-v5
#
# 参考信息：
# 腾讯云云API SDK：Python 2.7至3.6版本 
# 安装文档参考：https://cloud.tencent.com/document/sdk/Python
#
# 腾讯云COSV5Python SDK, 目前可以支持Python2.6与Python2.7以及Python3.x
# 安装文档参考： https://cloud.tencent.com/document/product/436/12269
#
# 运行例子：
# python uploadasset.py  --local_path ./game_folder/

其中脚本中需要配置用户的认证信息，下面两个信息：

secret_id = 'xxxx'     # 替换为用户的secret_id
secret_key = 'yyyy'     # 替换为用户的secret_key
```

其中内部实际上调用了如下的请求，只不过是是以腾讯云SDK的方式进行的调用

Input: 

```
tccli gse GetUploadFederationToken --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AssetCredentials": {
            "TmpSecretId": "xxxx",
            "TmpSecretKey": "yyyy",
            "Token": "jAlJicYVxHStLs34mTFfnSxJ7YpYx2UFae79befda56accd665e0c14b6ea2a8a9qM30cu5FtylTrH9U6Dm89Vl-uZ3vkcIRHS1jA8I9JaMJnAkGDFr-dtMt8v0vO3XSsF_T_RTIQHfqgXpYyyf-mLywmF3kZ07Ub7xIDfQSjGPg9yQXs-nqv2cpnsOLCDTRR598VYgkgExE31vIn6Ca-lNruZhxDwKS1fvi7g75yyLzX0Ambr6sB-ULEF6ubycmuMXyjXM4lsuRCuswkrHxSZXlsYtNF-hLlzcQjU6R4qXO8ncqDxfcVhadCMso_U73RxVcqcH21aG9IlnrLDpYRVGAXpQ1tvsgvOOJBh1mcQV6ef5MVTJFePIUsS7E2Sm1Ivv3-dP1lfHbs-Igu1IyF2hT8-zzs8mFlLt3yfdzwtbBGqZMTW9b-4Y5kdMY-cOqoTxbqjdJKTPEtLwi6160CRaabqSaRKsAI6dhgTsbc2vR4piNvdQZgL8I3vVrRtfAC5a0yZFfmd1EXnJjuYl_ZV78fNBC1VqVWDvWMyckJRZ2TepIItZR26FMkCsbFSTA7m5HN-nvRpo96WVsHy6QeJC9dpZbkHOePDRzZrXLRV_CHjiKn1wozZiNQ2kdDt_j"
        },
        "ExpiredTime": 1597058405,
        "RequestId": "a2b2a551-1551-4625-8ae9-086328d366b7"
    }
}
```

