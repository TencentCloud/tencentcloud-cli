**Example 1: 创建异步审核任务示例**

创建异步审核任务示例

Input: 

```
tccli ims CreateImageModerationAsyncTask --cli-unfold-argument  \
    --DataId test_data \
    --BizType brookyu_console_test \
    --FileUrl https://test.jpg \
    --CallbackUrl http://xxx.com
```

Output: 
```
{
    "Response": {
        "RequestId": "193101e1-e9b6-4a9b-b29e-6e37db58beef",
        "DataId": "test_data"
    }
}
```

