**Example 1: 创建PDF拆分任务**

对外部在线文档进行拆分

Input: 

```
tccli lkeap CreateSplitDocumentFlow --cli-unfold-argument  \
    --FileType PDF \
    --FileUrl https://fileparser-1251316161.cos.ap-guangzhou.myqcloud.com/input_files/oaqbot/%E8%87%AA%E7%84%B6%E8%AF%AD%E8%A8%80%E5%A4%84%E7%90%86%E7%BB%BC%E8%BF%B0-2020.pdf?q-sign-algorithm=sha1&q-ak=AKIDgh93rnqd2Gna1Nx7jyYsLQeGKB0hDq-0StLupLCJE_Yok5D1jR8oh4EjmPqUVN6b&q-sign-time=1725274092;1725277692&q-key-time=1725274092;1725277692&q-header-list=host&q-url-param-list=&q-signature=209b00a3abaeb3860400b27ae0e76dd41b817ad8&x-cos-security-token=3IoVMfyN7IlIDdke4rvTv7lnxYNl4g6ae86062408d0a5974e1d434912c363f0bCouWlELQpa4WAdO5u7ME8A3Ej_5XNnJ-8wK6AaeOVuzF4J1eTg3mBEDncaOMbOdeCAnRMCFOVEayNXIr_FYJL_LA54-Dm9a6x7pHUM-M0fQdkhNqFIzWBdoNr7nQnQEdJsFB5A_AfoQVl4f-jXJzqwuWBz7zv3KEEc6rO6770zgOHRJRnJBccBVdvqJUAJhv \
    --FileStartPageNumber 1 \
    --FileEndPageNumber 2 \
    --Config.TableResultType 1 \
    --Config.ResultType 1 \
    --Config.EnableMllm True \
    --FileName myfile.pdf
```

Output: 
```
{
    "Response": {
        "RequestId": "5e148c27-9c21-43cd-992c-799117bb4216",
        "TaskId": "a04cb05d5f794a5089e5b2cf90109bc5"
    }
}
```

