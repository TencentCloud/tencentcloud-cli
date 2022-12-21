**Example 1: 修改审核模板**

去掉广告检测，只保留涉黄、涉暴检测。

Input: 

```
tccli vod ModifyReviewTemplate --cli-unfold-argument  \
    --Definition 20123 \
    --Comment 开启涉黄、涉暴检测 \
    --Labels Porn Terror
```

Output: 
```
{
    "Response": {
        "RequestId": "67ae8d8e-dce3-4151-9d4b-5594145287e2"
    }
}
```

